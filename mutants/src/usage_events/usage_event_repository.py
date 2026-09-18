from abc import ABC, abstractmethod
from typing import override

from sqlalchemy.orm import Session

from usage_events.usage_event import UsageEvent
from usage_events.usage_event_model import UsageEventModel


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class UsageEventRepository(ABC):
    @abstractmethod
    def save(self, event: UsageEvent) -> None:
        raise NotImplementedError
mutants_xǁPostgresUsageEventRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore


class PostgresUsageEventRepository(UsageEventRepository):
    @_mutmut_mutated(mutants_xǁPostgresUsageEventRepositoryǁ__init____mutmut)
    def __init__(self, session: Session) -> None:
        self._session = session
    def xǁPostgresUsageEventRepositoryǁ__init____mutmut_orig(self, session: Session) -> None:
        self._session = session
    def xǁPostgresUsageEventRepositoryǁ__init____mutmut_1(self, session: Session) -> None:
        self._session = None

    @override
    def save(self, event: UsageEvent) -> None:
        table_row = UsageEventModel.from_domain(event)
        self._session.add(table_row)
        self._session.commit()

mutants_xǁPostgresUsageEventRepositoryǁ__init____mutmut['_mutmut_orig'] = PostgresUsageEventRepository.xǁPostgresUsageEventRepositoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPostgresUsageEventRepositoryǁ__init____mutmut['xǁPostgresUsageEventRepositoryǁ__init____mutmut_1'] = PostgresUsageEventRepository.xǁPostgresUsageEventRepositoryǁ__init____mutmut_1 # type: ignore # mutmut generated
