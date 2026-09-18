import pytest
from expects import expect, have_length

from test.usage_events.fake_uuid_generator import FakeUuidGenerator
from test.usage_events.in_memory_usage_event_repository import InMemoryUsageEventRepository
from test.usage_events.usage_event_mother import UsageEventMother
from usage_events.usage_event_register import UsageEventRegister


@pytest.mark.unit
class TestUsageEventRegister:
    def test_should_register_usage_event(self) -> None:
        usage_event = UsageEventMother.dummy()
        usage_event_repository = InMemoryUsageEventRepository()
        register = UsageEventRegister(
            repository=usage_event_repository,
            uuid_generator=FakeUuidGenerator(uuid_value=usage_event["id"]),
        )

        register.execute(**{key: value for key, value in usage_event.items() if key != "id"})

        expect(usage_event_repository).to(have_length(1))
