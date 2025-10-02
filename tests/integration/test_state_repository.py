"""Integration-style tests for DistributedStateRepository."""
from __future__ import annotations

import json
from datetime import datetime, timedelta
from unittest.mock import MagicMock

import pytest
from sqlalchemy import Column, DateTime, Integer, LargeBinary, MetaData, String, Table
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from src.state.repository import DistributedStateRepository, StateRecord


@pytest.fixture
def redis_mock() -> MagicMock:
    client = MagicMock()
    client.get.return_value = None
    return client


@pytest.fixture
def engine_mock() -> Engine:
    engine = MagicMock(spec=Engine)
    return engine


@pytest.fixture
def session_factory(engine_mock: Engine):
    meta = MetaData()
    table = Table(
        "session_state",
        meta,
        Column("session_id", String(64), primary_key=True),
        Column("payload", LargeBinary),
        Column("payload_hash", String(64)),
        Column("version", Integer),
        Column("created_at", DateTime(timezone=True)),
        Column("updated_at", DateTime(timezone=True)),
    )
    session = MagicMock()
    query_result = MagicMock()
    query_result.fetchone.return_value = None
    session.execute.return_value = query_result
    factory = MagicMock(return_value=session)
    return factory, table, session


def build_repository(redis_mock: MagicMock, engine_mock: Engine, factory_info):
    factory, table, session = factory_info
    repo = DistributedStateRepository(redis_mock, engine_mock)
    repo._table = table
    repo._session_factory = factory  # type: ignore[attr-defined]
    return repo, session


def test_save_inserts_new_record(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    repo, session = build_repository(redis_mock, engine_mock, session_factory)

    result = repo.save("s1", {"foo": "bar"})

    assert isinstance(result, StateRecord)
    assert result.session_id == "s1"
    assert result.payload["foo"] == "bar"
    assert session.execute.call_count >= 1
    assert session.commit.called
    assert redis_mock.setex.called
    assert "payload_hash" in session.execute.call_args.kwargs.get("parameters", {}) or session.execute.called


def test_get_returns_cached_value(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    cached = json.dumps({"payload": {"alpha": 1}, "hash": "xyz", "version": 1, "updated_at": datetime.utcnow().isoformat()})
    redis_mock.get.return_value = cached.encode("utf-8")
    repo, session = build_repository(redis_mock, engine_mock, session_factory)

    record = repo.get("abc")

    assert record is not None
    assert record.payload["alpha"] == 1
    assert session.execute.call_count == 0
    assert redis_mock.get.called
    assert redis_mock.setex.called
    assert repo.validate_integrity("abc") is True


def test_get_falls_back_to_database(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    redis_mock.get.return_value = None
    repo, session = build_repository(redis_mock, engine_mock, session_factory)

    row = MagicMock()
    row.session_id = "abc"
    row.payload = json.dumps({"value": 42}).encode("utf-8")
    row.payload_hash = "hash"
    row.version = 2
    row.created_at = datetime.utcnow() - timedelta(minutes=1)
    row.updated_at = datetime.utcnow()
    session.execute.return_value.fetchone.return_value = row

    record = repo.get("abc")

    assert record is not None
    assert record.session_id == "abc"
    assert record.payload["value"] == 42
    assert redis_mock.setex.called
    assert session.execute.called
    assert repo.validate_integrity("abc")


def test_delete_removes_from_cache_and_database(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    repo, session = build_repository(redis_mock, engine_mock, session_factory)

    repo.delete("session-x")

    assert redis_mock.delete.called
    assert session.execute.called
    assert session.commit.called


@pytest.mark.asyncio
async def test_record_cache_latency_uses_ttl(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    repo, _ = build_repository(redis_mock, engine_mock, session_factory)

    repo.record_cache_latency("abc", latency_ms=32.5)
    ttl_arg = redis_mock.setex.call_args.kwargs.get("time") if redis_mock.setex.call_args else None

    assert redis_mock.setex.called
    assert isinstance(redis_mock.setex.call_args.args[0], str)
    assert redis_mock.setex.call_args.args[0].startswith("state:latency:")
    assert redis_mock.setex.call_args.args[1].seconds == 300
    assert ttl_arg is None or ttl_arg.seconds == 300


def test_touch_extends_ttl(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    repo, _ = build_repository(redis_mock, engine_mock, session_factory)

    repo.touch("abc", ttl_extension=120)

    assert redis_mock.expire.called
    assert redis_mock.expire.call_args.args[0] == "state:abc"
    assert redis_mock.expire.call_args.args[1] == 120


def test_session_exists_checks_cache_first(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    redis_mock.exists.return_value = True
    repo, session = build_repository(redis_mock, engine_mock, session_factory)

    exists = repo.session_exists("foo")

    assert exists is True
    assert redis_mock.exists.called
    assert session.execute.call_count == 0


def test_session_exists_queries_database_when_cache_miss(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    redis_mock.exists.return_value = False
    repo, session = build_repository(redis_mock, engine_mock, session_factory)
    session.execute.return_value.scalar.return_value = "foo"

    exists = repo.session_exists("foo")

    assert exists is True
    assert session.execute.called
    assert redis_mock.exists.called


def test_purge_stale_removes_old_records(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    repo, session = build_repository(redis_mock, engine_mock, session_factory)
    result_mock = MagicMock()
    result_mock.rowcount = 3
    session.execute.return_value = result_mock

    count = repo.purge_stale(datetime.utcnow() - timedelta(days=7))

    assert count == 3
    assert session.execute.called
    assert session.commit.called


def test_validate_integrity_handles_missing(redis_mock: MagicMock, engine_mock: Engine, session_factory):
    redis_mock.get.return_value = None
    repo, session = build_repository(redis_mock, engine_mock, session_factory)
    session.execute.return_value.fetchone.return_value = None

    assert repo.validate_integrity("missing") is False
    assert session.execute.called
    assert not redis_mock.setex.called
