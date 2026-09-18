from typing import TypedDict


class UsageEvent(TypedDict):
    id: str
    user_id: str
    ipy_version: str
    python_version: str
    operating_system: str
    command: str
    dependency_manager: str
    template: str
    built_in_features: list[str]
