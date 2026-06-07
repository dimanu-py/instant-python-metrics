"""Usage event domain entity."""

from dataclasses import dataclass, field
from uuid import UUID

from uuid_extensions import uuid7


@dataclass
class UsageEvent:
    """A usage event representing a CLI invocation."""

    event_id: UUID = field(default_factory=uuid7)
    ipy_version: str = ""
    operating_system: str = ""
    distinct_id: str = ""
    command: str = ""
    python_version: str = ""
    dependency_manager: str = ""
    template: str = ""
    built_in_features: list[str] = field(default_factory=list)
