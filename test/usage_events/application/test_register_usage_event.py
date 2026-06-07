"""Application unit tests for RegisterUsageEventUseCase."""

from typing import Any

import pytest
from doublex import ANY_ARG, Mock, expect_call
from expects import be_none, equal, expect, have_properties

from usage_events.application.register_usage_event import RegisterUsageEventUseCase
from usage_events.domain.usage_event import UsageEvent
from usage_events.domain.usage_event_repository import UsageEventRepository


@pytest.mark.unit
class TestRegisterUsageEventUseCase:
    """Tests for the RegisterUsageEventUseCase orchestration."""

    def test_saves_event_with_all_field_values(self) -> None:
        """The use case must construct a UsageEvent with all field values and save it."""
        repository: Any = Mock(UsageEventRepository)
        expect_call(repository).save(ANY_ARG)
        use_case = RegisterUsageEventUseCase(repository)

        event_id = use_case.execute(
            ipy_version="1.2.3",
            operating_system="linux",
            distinct_id="a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            command="generate",
            python_version="3.13.1",
            dependency_manager="uv",
            template="standard_project",
            built_in_features=["github_actions"],
        )

        expect(event_id).to_not(be_none)
        saved_event: UsageEvent = repository.save.calls[0].args[0]
        expect(saved_event).to(
            have_properties(
                ipy_version="1.2.3",
                operating_system="linux",
                distinct_id="a1b2c3d4-e5f6-4789-abcd-ef1234567890",
                command="generate",
                python_version="3.13.1",
                dependency_manager="uv",
                template="standard_project",
                built_in_features=["github_actions"],
            )
        )

    def test_returns_event_id_matching_saved_event(self) -> None:
        """The returned UUID must match the ID of the event saved in the repository."""
        repository: Any = Mock(UsageEventRepository)
        expect_call(repository).save(ANY_ARG)
        use_case = RegisterUsageEventUseCase(repository)

        event_id = use_case.execute(
            ipy_version="1.2.3",
            operating_system="linux",
            distinct_id="a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            command="generate",
            python_version="3.13.1",
            dependency_manager="uv",
            template="standard_project",
            built_in_features=["github_actions"],
        )

        saved_event: UsageEvent = repository.save.calls[0].args[0]
        expect(saved_event.event_id).to(equal(event_id))

    def test_saves_event_with_empty_built_in_features(self) -> None:
        """The use case must handle an empty built_in_features list."""
        repository: Any = Mock(UsageEventRepository)
        expect_call(repository).save(ANY_ARG)
        use_case = RegisterUsageEventUseCase(repository)

        event_id = use_case.execute(
            ipy_version="1.2.3",
            operating_system="linux",
            distinct_id="a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            command="generate",
            python_version="3.13.1",
            dependency_manager="uv",
            template="standard_project",
            built_in_features=[],
        )

        expect(event_id).to_not(be_none)
        saved_event: UsageEvent = repository.save.calls[0].args[0]
        expect(saved_event.built_in_features).to(equal([]))
