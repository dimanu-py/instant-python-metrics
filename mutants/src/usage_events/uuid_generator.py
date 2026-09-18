from abc import ABC, abstractmethod
from typing import override

from uuid_extensions import uuid7str


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class UuidGenerator(ABC):
    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError


class Uuid7Generator(UuidGenerator):
    @override
    def generate(self) -> str:
        return uuid7str()
