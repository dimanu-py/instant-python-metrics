from usage_events.usage_event import UsageEvent
from usage_events.usage_event_repository import UsageEventRepository
from usage_events.uuid_generator import UuidGenerator


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁUsageEventRegisterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁUsageEventRegisterǁexecute__mutmut: MutantDict = {}  # type: ignore


class UsageEventRegister:
    @_mutmut_mutated(mutants_xǁUsageEventRegisterǁ__init____mutmut)
    def __init__(self, repository: UsageEventRepository, uuid_generator: UuidGenerator) -> None:
        self._repository = repository
        self._uuid_generator = uuid_generator
    def xǁUsageEventRegisterǁ__init____mutmut_orig(self, repository: UsageEventRepository, uuid_generator: UuidGenerator) -> None:
        self._repository = repository
        self._uuid_generator = uuid_generator
    def xǁUsageEventRegisterǁ__init____mutmut_1(self, repository: UsageEventRepository, uuid_generator: UuidGenerator) -> None:
        self._repository = None
        self._uuid_generator = uuid_generator
    def xǁUsageEventRegisterǁ__init____mutmut_2(self, repository: UsageEventRepository, uuid_generator: UuidGenerator) -> None:
        self._repository = repository
        self._uuid_generator = None

    @_mutmut_mutated(mutants_xǁUsageEventRegisterǁexecute__mutmut)
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

    def xǁUsageEventRegisterǁexecute__mutmut_orig(
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

    def xǁUsageEventRegisterǁexecute__mutmut_1(
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
        usage_event = None
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_2(
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
            id=None,
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

    def xǁUsageEventRegisterǁexecute__mutmut_3(
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
            user_id=None,
            ipy_version=ipy_version,
            python_version=python_version,
            operating_system=operating_system,
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_4(
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
            ipy_version=None,
            python_version=python_version,
            operating_system=operating_system,
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_5(
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
            python_version=None,
            operating_system=operating_system,
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_6(
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
            operating_system=None,
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_7(
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
            command=None,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_8(
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
            dependency_manager=None,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_9(
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
            template=None,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_10(
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
            built_in_features=None,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_11(
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

    def xǁUsageEventRegisterǁexecute__mutmut_12(
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
            ipy_version=ipy_version,
            python_version=python_version,
            operating_system=operating_system,
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_13(
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
            python_version=python_version,
            operating_system=operating_system,
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_14(
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
            operating_system=operating_system,
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_15(
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
            command=command,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_16(
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
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_17(
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
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_18(
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
            built_in_features=built_in_features,
        )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_19(
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
            )
        self._repository.save(usage_event)

    def xǁUsageEventRegisterǁexecute__mutmut_20(
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
        self._repository.save(None)

mutants_xǁUsageEventRegisterǁ__init____mutmut['_mutmut_orig'] = UsageEventRegister.xǁUsageEventRegisterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁ__init____mutmut['xǁUsageEventRegisterǁ__init____mutmut_1'] = UsageEventRegister.xǁUsageEventRegisterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁ__init____mutmut['xǁUsageEventRegisterǁ__init____mutmut_2'] = UsageEventRegister.xǁUsageEventRegisterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁUsageEventRegisterǁexecute__mutmut['_mutmut_orig'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_1'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_2'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_3'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_4'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_5'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_6'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_7'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_8'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_9'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_10'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_11'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_12'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_13'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_14'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_15'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_16'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_17'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_18'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_19'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUsageEventRegisterǁexecute__mutmut['xǁUsageEventRegisterǁexecute__mutmut_20'] = UsageEventRegister.xǁUsageEventRegisterǁexecute__mutmut_20 # type: ignore # mutmut generated
