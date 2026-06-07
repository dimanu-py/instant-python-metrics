"""Infra unit tests for MemoryUsageEventRepository."""

import pytest
from expects import be_none, equal, expect

from usage_events.domain.usage_event import UsageEvent
from usage_events.infra.memory_usage_event_repository import MemoryUsageEventRepository


@pytest.mark.unit
class TestMemoryUsageEventRepository:
    """Tests for the in-memory usage event repository."""

    def test_stores_event_and_preserves_fields(self) -> None:
        """The repository must store and preserve all field values."""
        repository = MemoryUsageEventRepository()
        event = UsageEvent(
            ipy_version="1.2.3",
            operating_system="linux",
            distinct_id="a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            command="generate",
            python_version="3.13.1",
            dependency_manager="uv",
            template="standard_project",
            built_in_features=["github_actions"],
        )

        repository.save(event)

        # Access internal storage to verify the event was stored correctly
        stored_events = repository._events
        expect(len(stored_events)).to(equal(1))
        stored = stored_events[0]
        expect(stored.ipy_version).to(equal("1.2.3"))
        expect(stored.operating_system).to(equal("linux"))
        expect(stored.distinct_id).to(equal("a1b2c3d4-e5f6-4789-abcd-ef1234567890"))
        expect(stored.command).to(equal("generate"))
        expect(stored.python_version).to(equal("3.13.1"))
        expect(stored.dependency_manager).to(equal("uv"))
        expect(stored.template).to(equal("standard_project"))
        expect(stored.built_in_features).to(equal(["github_actions"]))
        expect(stored.event_id).to_not(be_none)

    def test_stores_multiple_events(self) -> None:
        """The repository must store multiple events."""
        repository = MemoryUsageEventRepository()
        event1 = UsageEvent(ipy_version="1.0.0", command="init")
        event2 = UsageEvent(ipy_version="2.0.0", command="generate")

        repository.save(event1)
        repository.save(event2)

        expect(len(repository._events)).to(equal(2))
