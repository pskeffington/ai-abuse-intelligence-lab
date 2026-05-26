"""Domain models for defensive AI-abuse intelligence analysis."""

from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field, HttpUrl


class ConfidenceLevel(StrEnum):
    """Analyst confidence levels for observations and assessments."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class EventType(StrEnum):
    """Normalized event categories for abuse-intelligence workflows."""

    CONTENT_POST = "content_post"
    ACCOUNT_ACTION = "account_action"
    COORDINATION_SIGNAL = "coordination_signal"
    MODEL_OUTPUT = "model_output"
    PLATFORM_REPORT = "platform_report"
    EXTERNAL_REFERENCE = "external_reference"


class SourceRef(BaseModel):
    """Reference to the provenance for an observation."""

    source_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    url: HttpUrl | None = None
    collected_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    notes: str | None = None


class Actor(BaseModel):
    """Observed entity involved in an event."""

    actor_id: str = Field(default_factory=lambda: str(uuid4()))
    handle: str | None = None
    platform: str | None = None
    attributes: dict[str, Any] = Field(default_factory=dict)


class Artifact(BaseModel):
    """Content, media, or technical object associated with an event."""

    artifact_id: str = Field(default_factory=lambda: str(uuid4()))
    artifact_type: str
    value: str
    hash_value: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class AbuseEvent(BaseModel):
    """Normalized event used by ingestion, analysis, and reporting layers."""

    event_id: str = Field(default_factory=lambda: str(uuid4()))
    event_type: EventType
    observed_at: datetime
    source: SourceRef
    actor: Actor | None = None
    artifact: Artifact | None = None
    confidence: ConfidenceLevel = ConfidenceLevel.MEDIUM
    tags: list[str] = Field(default_factory=list)
    narrative: str = ""


class Finding(BaseModel):
    """Analyst-facing assessment generated from one or more events."""

    finding_id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    summary: str
    confidence: ConfidenceLevel
    related_event_ids: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
