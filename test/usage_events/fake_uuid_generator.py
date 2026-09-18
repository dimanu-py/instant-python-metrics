from typing import override

from usage_events.uuid_generator import UuidGenerator


class FakeUuidGenerator(UuidGenerator):
    def __init__(self, uuid_value: str) -> None:
        self._uuid = uuid_value

    @override
    def generate(self) -> str:
        return self._uuid
