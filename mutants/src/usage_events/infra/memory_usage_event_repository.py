"""In-memory implementation of UsageEventRepository for development."""

from usage_events.domain.usage_event import UsageEvent
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


class MemoryUsageEventRepository:
    """In-memory repository for usage events (non-persistent)."""

    def __init__(self) -> None:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMemoryUsageEventRepositoryǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁMemoryUsageEventRepositoryǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁMemoryUsageEventRepositoryǁ__init____mutmut_orig(self) -> None:
        self._events: list[UsageEvent] = []

    def xǁMemoryUsageEventRepositoryǁ__init____mutmut_1(self) -> None:
        self._events: list[UsageEvent] = None
    
    xǁMemoryUsageEventRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMemoryUsageEventRepositoryǁ__init____mutmut_1': xǁMemoryUsageEventRepositoryǁ__init____mutmut_1
    }
    xǁMemoryUsageEventRepositoryǁ__init____mutmut_orig.__name__ = 'xǁMemoryUsageEventRepositoryǁ__init__'

    def save(self, event: UsageEvent) -> None:
        args = [event]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMemoryUsageEventRepositoryǁsave__mutmut_orig'), object.__getattribute__(self, 'xǁMemoryUsageEventRepositoryǁsave__mutmut_mutants'), args, kwargs, self)

    def xǁMemoryUsageEventRepositoryǁsave__mutmut_orig(self, event: UsageEvent) -> None:
        self._events.append(event)

    def xǁMemoryUsageEventRepositoryǁsave__mutmut_1(self, event: UsageEvent) -> None:
        self._events.append(None)
    
    xǁMemoryUsageEventRepositoryǁsave__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMemoryUsageEventRepositoryǁsave__mutmut_1': xǁMemoryUsageEventRepositoryǁsave__mutmut_1
    }
    xǁMemoryUsageEventRepositoryǁsave__mutmut_orig.__name__ = 'xǁMemoryUsageEventRepositoryǁsave'
