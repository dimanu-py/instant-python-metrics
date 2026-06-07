"""PostgreSQL implementation of UsageEventRepository."""

from sqlalchemy.orm import Session

from usage_events.domain.usage_event import UsageEvent
from usage_events.infra.models import UsageEventModel
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


class PostgresUsageEventRepository:
    """PostgreSQL-backed usage event repository."""

    def __init__(self, session: Session) -> None:
        args = [session]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPostgresUsageEventRepositoryǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁPostgresUsageEventRepositoryǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁPostgresUsageEventRepositoryǁ__init____mutmut_orig(self, session: Session) -> None:
        self._session = session

    def xǁPostgresUsageEventRepositoryǁ__init____mutmut_1(self, session: Session) -> None:
        self._session = None
    
    xǁPostgresUsageEventRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPostgresUsageEventRepositoryǁ__init____mutmut_1': xǁPostgresUsageEventRepositoryǁ__init____mutmut_1
    }
    xǁPostgresUsageEventRepositoryǁ__init____mutmut_orig.__name__ = 'xǁPostgresUsageEventRepositoryǁ__init__'

    def save(self, event: UsageEvent) -> None:
        args = [event]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPostgresUsageEventRepositoryǁsave__mutmut_orig'), object.__getattribute__(self, 'xǁPostgresUsageEventRepositoryǁsave__mutmut_mutants'), args, kwargs, self)

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_orig(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_1(self, event: UsageEvent) -> None:
        model = None
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_2(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=None,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_3(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=None,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_4(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=None,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_5(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=None,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_6(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=None,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_7(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=None,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_8(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=None,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_9(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=None,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_10(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=None,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_11(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_12(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_13(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_14(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_15(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_16(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_17(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_18(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_19(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            )
        self._session.add(model)
        self._session.commit()

    def xǁPostgresUsageEventRepositoryǁsave__mutmut_20(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(None)
        self._session.commit()
    
    xǁPostgresUsageEventRepositoryǁsave__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPostgresUsageEventRepositoryǁsave__mutmut_1': xǁPostgresUsageEventRepositoryǁsave__mutmut_1, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_2': xǁPostgresUsageEventRepositoryǁsave__mutmut_2, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_3': xǁPostgresUsageEventRepositoryǁsave__mutmut_3, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_4': xǁPostgresUsageEventRepositoryǁsave__mutmut_4, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_5': xǁPostgresUsageEventRepositoryǁsave__mutmut_5, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_6': xǁPostgresUsageEventRepositoryǁsave__mutmut_6, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_7': xǁPostgresUsageEventRepositoryǁsave__mutmut_7, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_8': xǁPostgresUsageEventRepositoryǁsave__mutmut_8, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_9': xǁPostgresUsageEventRepositoryǁsave__mutmut_9, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_10': xǁPostgresUsageEventRepositoryǁsave__mutmut_10, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_11': xǁPostgresUsageEventRepositoryǁsave__mutmut_11, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_12': xǁPostgresUsageEventRepositoryǁsave__mutmut_12, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_13': xǁPostgresUsageEventRepositoryǁsave__mutmut_13, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_14': xǁPostgresUsageEventRepositoryǁsave__mutmut_14, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_15': xǁPostgresUsageEventRepositoryǁsave__mutmut_15, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_16': xǁPostgresUsageEventRepositoryǁsave__mutmut_16, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_17': xǁPostgresUsageEventRepositoryǁsave__mutmut_17, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_18': xǁPostgresUsageEventRepositoryǁsave__mutmut_18, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_19': xǁPostgresUsageEventRepositoryǁsave__mutmut_19, 
        'xǁPostgresUsageEventRepositoryǁsave__mutmut_20': xǁPostgresUsageEventRepositoryǁsave__mutmut_20
    }
    xǁPostgresUsageEventRepositoryǁsave__mutmut_orig.__name__ = 'xǁPostgresUsageEventRepositoryǁsave'
