"""Async notification publisher supporting multiple channels."""
from __future__ import annotations

import asyncio
import json
import logging
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Optional

import httpx

LOGGER = logging.getLogger(__name__)


@dataclass
class NotificationMessage:
    """Represents a message scheduled for delivery."""

    destination: str
    payload: Dict[str, Any]
    channel: str
    correlation_id: str
    trace_id: str


class NotificationError(RuntimeError):
    """Raised when notification delivery fails."""


class NotificationPublisher:
    """Publishes notifications to webhooks, Slack, and email."""

    def __init__(self, http_client: Optional[httpx.AsyncClient] = None) -> None:
        self._client = http_client or httpx.AsyncClient()
        self._hooks: Dict[str, str] = {}
        self._history: List[NotificationMessage] = []

    def register_channel(self, name: str, endpoint: str) -> None:
        """Register a channel endpoint for outbound notifications."""

        self._hooks[name] = endpoint

    async def _post(self, endpoint: str, payload: Dict[str, Any]) -> httpx.Response:
        """Send an HTTP POST request via httpx."""

        LOGGER.debug("POST %s payload=%s", endpoint, payload)
        return await self._client.post(endpoint, json=payload, timeout=5.0)

    def _build_message(self, channel: str, destination: str, payload: Dict[str, Any]) -> NotificationMessage:
        """Construct a NotificationMessage with correlation metadata."""

        correlation_id = str(uuid.uuid4())
        trace_id = str(uuid.uuid4())
        enriched_payload = dict(payload)
        enriched_payload.update({
            "correlation_id": correlation_id,
            "trace_id": trace_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        return NotificationMessage(
            destination=destination,
            payload=enriched_payload,
            channel=channel,
            correlation_id=correlation_id,
            trace_id=trace_id,
        )

    async def publish(self, channel: str, payload: Dict[str, Any]) -> NotificationMessage:
        """Publish a single notification to the configured channel."""

        if channel not in self._hooks:
            raise NotificationError(f"Channel {channel} not registered")
        endpoint = self._hooks[channel]
        message = self._build_message(channel, endpoint, payload)
        response = await self._post(endpoint, message.payload)
        if response.status_code >= 400:
            raise NotificationError(f"Notification failed: {response.status_code}")
        self._history.append(message)
        LOGGER.info(
            "Delivered notification to %s correlation=%s trace_id=%s",
            endpoint,
            message.correlation_id,
            message.trace_id,
        )
        return message

    async def publish_bulk(self, channel: str, payloads: Iterable[Dict[str, Any]]) -> List[NotificationMessage]:
        """Publish multiple notifications concurrently."""

        tasks = [self.publish(channel, payload) for payload in payloads]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        delivered: List[NotificationMessage] = []
        for result in results:
            if isinstance(result, NotificationMessage):
                delivered.append(result)
            else:
                LOGGER.error("Bulk notification failure: %s", result)
        return delivered

    def history(self) -> List[NotificationMessage]:
        """Return delivery history."""

        return list(self._history)

    async def close(self) -> None:
        """Close the underlying httpx AsyncClient."""

        await self._client.aclose()

    def export_history(self) -> str:
        """Return history as JSON string for evidence exports."""

        return json.dumps([message.__dict__ for message in self._history], indent=2)


__all__ = ["NotificationPublisher", "NotificationMessage", "NotificationError"]
