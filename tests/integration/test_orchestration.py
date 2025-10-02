"""Integration tests for the LangGraph coordination graph."""
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

langgraph = pytest.importorskip("langgraph")

from src.orchestration import graph_builder


@pytest.fixture
def context_factory():
    def _factory():
        return graph_builder.initialise_context({"type": "coding", "details": {"planner": True}})
    return _factory


def test_build_graph_contains_required_nodes(context_factory):
    graph = graph_builder.build_graph()

    assert "planner" in graph.nodes
    assert "coder" in graph.nodes
    assert "critic" in graph.nodes
    assert "qa" in graph.nodes
    assert "approver" in graph.nodes


def test_execute_workflow_sets_approval(context_factory):
    context = graph_builder.initialise_context({"type": "planning"})
    graph = graph_builder.build_graph()
    executor = graph_builder.build_executor(graph)

    result = executor(context)

    assert result.state.get("approved") is True
    assert "approvals" in result.events
    assert result.events["history"][0] == "planner_completed"
    assert result.state["qa_passed"]


def test_refinement_condition_triggers_loop(monkeypatch, context_factory):
    context = context_factory()
    context.state["needs_revision"] = True

    outcome = graph_builder.refinement_condition(context)

    assert outcome == "refine"


def test_conditional_edges_support_refinement(monkeypatch):
    graph = graph_builder.build_graph()
    mock_executor = MagicMock(side_effect=lambda ctx: ctx)
    monkeypatch.setattr(graph, "compile", lambda: mock_executor)

    executor = graph_builder.build_executor(graph)
    context = graph_builder.initialise_context({"type": "coding"})
    context.state["needs_revision"] = False

    result = executor(context)

    assert mock_executor.called
    assert isinstance(result.state, dict)
    assert "task" in result.state


def test_execute_workflow_handles_budget_metadata(monkeypatch):
    context = graph_builder.initialise_context({"type": "coding", "budget": {"daily": 450}})

    class DummyExecutor:
        def __call__(self, ctx):
            ctx.state["approved"] = True
            ctx.events.setdefault("policy", []).append({"budget": ctx.state["task"].get("budget", {})})
            return ctx

    graph = graph_builder.build_graph()
    monkeypatch.setattr(graph, "compile", lambda: DummyExecutor())

    result = graph_builder.execute_workflow({"type": "coding", "budget": {"daily": 200}})

    assert result.state["approved"] is True
    assert result.events["policy"][0]["budget"]["daily"] == 200
    assert "policy" in result.events


def test_initialise_context_sets_defaults():
    context = graph_builder.initialise_context({"type": "qa", "budget": {"monthly": 12000}})

    assert context.state["task"]["type"] == "qa"
    assert context.events == {}
    assert "budget" in context.state["task"]
    assert context.state["task"]["budget"]["monthly"] == 12000


def test_refinement_loop_returns_proceed(monkeypatch, context_factory):
    context = context_factory()
    context.state["needs_revision"] = False

    decision = graph_builder.refinement_condition(context)

    assert decision == "proceed"


def test_executor_logs_completion(monkeypatch, caplog):
    caplog.set_level("INFO")
    context = graph_builder.initialise_context({"type": "qa", "budget": {"daily": 100}})
    graph = graph_builder.build_graph()

    class DummyCallable:
        def __call__(self, ctx):
            ctx.state["approved"] = True
            ctx.events.setdefault("approvals", []).append("approved")
            return ctx

    monkeypatch.setattr(graph, "compile", lambda: DummyCallable())

    result = graph_builder.execute_workflow({"type": "qa", "budget": {"daily": 100}})

    assert result.state["approved"] is True
    assert "approved" in result.events["approvals"][0]
    assert any("Workflow completed" in message for message in caplog.messages)


def test_graph_executor_handles_multiple_calls(monkeypatch):
    graph = graph_builder.build_graph()

    class DummyCallable:
        def __call__(self, ctx):
            ctx.state.setdefault("runs", 0)
            ctx.state["runs"] += 1
            ctx.events.setdefault("history", []).append("qa_checked")
            ctx.state["approved"] = True
            return ctx

    monkeypatch.setattr(graph, "compile", lambda: DummyCallable())

    result_one = graph_builder.execute_workflow({"type": "coding"})
    result_two = graph_builder.execute_workflow({"type": "planning"})

    assert result_one.state["approved"]
    assert result_two.state["approved"]
    assert len(result_two.events["history"]) >= 1
    assert "qa_checked" in result_two.events["history"]
