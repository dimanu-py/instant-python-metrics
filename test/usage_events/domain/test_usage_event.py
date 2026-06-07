"""Domain unit tests for UsageEvent."""

import pytest
from expects import equal, expect
from uuid_extensions import uuid7

from usage_events.domain.usage_event import UsageEvent


@pytest.mark.unit
class TestUsageEvent:
    """Tests for the UsageEvent domain entity."""

    def test_event_id_is_uuid_v7(self) -> None:
        """The event_id must be a UUID version 7."""
        event = UsageEvent()
        expect(event.event_id.version).to(equal(7))

    def test_event_id_can_be_generated_with_uuid7_library(self) -> None:
        """The uuid7 library must produce valid UUID v7."""
        uid = uuid7()
        expect(uid.version).to(equal(7))
