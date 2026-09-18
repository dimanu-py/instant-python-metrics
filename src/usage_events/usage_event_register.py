from usage_events.usage_event import UsageEvent
from usage_events.usage_event_repository import UsageEventRepository
from usage_events.uuid_generator import UuidGenerator


class UsageEventRegister:
    def __init__(self, repository: UsageEventRepository, uuid_generator: UuidGenerator) -> None:
        self._repository = repository
        self._uuid_generator = uuid_generator

    def execute(
        self,
        ipy_version: str,
        python_version: str,
        operating_system: str,
        user_id: str,
        command: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> None:
        usage_event = UsageEvent(
            id=self._uuid_generator.generate(),
            user_id=user_id,
            ipy_version=ipy_version,
            python_version=python_version,
            operating_system=operating_system,
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)
