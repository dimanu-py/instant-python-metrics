"""Use case for registering a usage event."""

from typing import cast
from uuid import UUID

from usage_events.domain.usage_event import UsageEvent
from usage_events.domain.usage_event_repository import UsageEventRepository
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


class RegisterUsageEventUseCase:
    def __init__(self, repository: UsageEventRepository) -> None:
        args = [repository]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁRegisterUsageEventUseCaseǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁRegisterUsageEventUseCaseǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁRegisterUsageEventUseCaseǁ__init____mutmut_orig(self, repository: UsageEventRepository) -> None:
        self._repository = repository
    def xǁRegisterUsageEventUseCaseǁ__init____mutmut_1(self, repository: UsageEventRepository) -> None:
        self._repository = None
    
    xǁRegisterUsageEventUseCaseǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁRegisterUsageEventUseCaseǁ__init____mutmut_1': xǁRegisterUsageEventUseCaseǁ__init____mutmut_1
    }
    xǁRegisterUsageEventUseCaseǁ__init____mutmut_orig.__name__ = 'xǁRegisterUsageEventUseCaseǁ__init__'

    def execute(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        args = [ipy_version, operating_system, distinct_id, command, python_version, dependency_manager, template, built_in_features]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁRegisterUsageEventUseCaseǁexecute__mutmut_orig'), object.__getattribute__(self, 'xǁRegisterUsageEventUseCaseǁexecute__mutmut_mutants'), args, kwargs, self)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_orig(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_1(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = None
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_2(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=None,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_3(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=None,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_4(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=None,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_5(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=None,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_6(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=None,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_7(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=None,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_8(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=None,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_9(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=None,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_10(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_11(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_12(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_13(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_14(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_15(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_16(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_17(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            )
        self._repository.save(event)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_18(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(None)
        return cast(UUID, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_19(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(None, event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_20(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, None)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_21(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(event.event_id)

    def xǁRegisterUsageEventUseCaseǁexecute__mutmut_22(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, )
    
    xǁRegisterUsageEventUseCaseǁexecute__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁRegisterUsageEventUseCaseǁexecute__mutmut_1': xǁRegisterUsageEventUseCaseǁexecute__mutmut_1, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_2': xǁRegisterUsageEventUseCaseǁexecute__mutmut_2, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_3': xǁRegisterUsageEventUseCaseǁexecute__mutmut_3, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_4': xǁRegisterUsageEventUseCaseǁexecute__mutmut_4, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_5': xǁRegisterUsageEventUseCaseǁexecute__mutmut_5, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_6': xǁRegisterUsageEventUseCaseǁexecute__mutmut_6, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_7': xǁRegisterUsageEventUseCaseǁexecute__mutmut_7, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_8': xǁRegisterUsageEventUseCaseǁexecute__mutmut_8, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_9': xǁRegisterUsageEventUseCaseǁexecute__mutmut_9, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_10': xǁRegisterUsageEventUseCaseǁexecute__mutmut_10, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_11': xǁRegisterUsageEventUseCaseǁexecute__mutmut_11, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_12': xǁRegisterUsageEventUseCaseǁexecute__mutmut_12, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_13': xǁRegisterUsageEventUseCaseǁexecute__mutmut_13, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_14': xǁRegisterUsageEventUseCaseǁexecute__mutmut_14, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_15': xǁRegisterUsageEventUseCaseǁexecute__mutmut_15, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_16': xǁRegisterUsageEventUseCaseǁexecute__mutmut_16, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_17': xǁRegisterUsageEventUseCaseǁexecute__mutmut_17, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_18': xǁRegisterUsageEventUseCaseǁexecute__mutmut_18, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_19': xǁRegisterUsageEventUseCaseǁexecute__mutmut_19, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_20': xǁRegisterUsageEventUseCaseǁexecute__mutmut_20, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_21': xǁRegisterUsageEventUseCaseǁexecute__mutmut_21, 
        'xǁRegisterUsageEventUseCaseǁexecute__mutmut_22': xǁRegisterUsageEventUseCaseǁexecute__mutmut_22
    }
    xǁRegisterUsageEventUseCaseǁexecute__mutmut_orig.__name__ = 'xǁRegisterUsageEventUseCaseǁexecute'
