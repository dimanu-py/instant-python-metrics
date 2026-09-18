from usage_events.usage_event import UsageEvent


class UsageEventMother:
    @staticmethod
    def dummy() -> UsageEvent:
        return UsageEventMother.with_id("06a2e698-4377-7f43-8000-0a4f8c034fd4")

    @staticmethod
    def with_id(event_id: str) -> UsageEvent:
        return UsageEvent(
            id=event_id,
            ipy_version="1.2.3",
            python_version="3.11",
            operating_system="Linux",
            user_id="550e8400-e29b-41d4-a716-446655440000",
            command="init",
            dependency_manager="uv",
            template="standard",
            built_in_features=["github_actions", "makefile"],
        )


class UsageEventMotherForPayload:
    _BASE_PAYLOAD = {
        "ipy_version": "1.2.3",
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "550e8400-e29b-41d4-a716-446655440000",
        "command": "init",
        "dependency_manager": "uv",
        "template": "standard",
        "built_in_features": ["github_actions", "makefile"],
    }

    @classmethod
    def dummy(cls) -> dict:
        return dict(cls._BASE_PAYLOAD)

    @classmethod
    def without_built_in_features_selected(cls) -> dict:
        return {**cls._BASE_PAYLOAD, "built_in_features": []}

    @classmethod
    def with_extra_unknown_fields(cls) -> dict:
        return {**cls._BASE_PAYLOAD, "extra_field_1": "value1", "extra_field_2": "value2"}

    @classmethod
    def with_missing_field(cls, field_name: str) -> dict:
        return {key: value for key, value in cls._BASE_PAYLOAD.items() if key != field_name}
