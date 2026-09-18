from datetime import UTC, datetime

from sqlalchemy import JSON, UUID, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from common.persistence.orm_base import OrmBase
from usage_events.usage_event import UsageEvent


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁUsageEventModelǁfrom_domain__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUsageEventModelǁto_domain__mutmut: MutantDict = {}  # type: ignore


class UsageEventModel(OrmBase):
    __tablename__ = "usage_events"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(256), nullable=False)
    ipy_version: Mapped[str] = mapped_column(String(256), nullable=False)
    python_version: Mapped[str] = mapped_column(String(256), nullable=False)
    operating_system: Mapped[str] = mapped_column(String(256), nullable=False)
    command: Mapped[str] = mapped_column(String(256), nullable=False)
    dependency_manager: Mapped[str] = mapped_column(String(256), nullable=False)
    template: Mapped[str] = mapped_column(String(256), nullable=False)
    built_in_features: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=lambda: datetime.now(UTC))

    @classmethod
    @_mutmut_mutated(mutants_xǁUsageEventModelǁfrom_domain__mutmut, is_classmethod = True)
    def from_domain(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_orig(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_1(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=None,
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_2(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=None,
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_3(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=None,
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_4(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=None,
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_5(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=None,
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_6(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=None,
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_7(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=None,
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_8(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=None,
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_9(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=None,
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_10(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_11(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_12(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_13(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_14(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_15(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_16(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_17(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_18(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_19(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["XXidXX"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_20(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["ID"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_21(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["XXuser_idXX"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_22(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["USER_ID"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_23(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["XXipy_versionXX"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_24(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["IPY_VERSION"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_25(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["XXpython_versionXX"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_26(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["PYTHON_VERSION"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_27(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["XXoperating_systemXX"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_28(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["OPERATING_SYSTEM"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_29(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["XXcommandXX"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_30(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["COMMAND"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_31(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["XXdependency_managerXX"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_32(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["DEPENDENCY_MANAGER"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_33(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["XXtemplateXX"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_34(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["TEMPLATE"],
            built_in_features=event["built_in_features"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_35(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["XXbuilt_in_featuresXX"],
        )

    @classmethod
    def xǁUsageEventModelǁfrom_domain__mutmut_36(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["BUILT_IN_FEATURES"],
        )

    @_mutmut_mutated(mutants_xǁUsageEventModelǁto_domain__mutmut)
    def to_domain(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_orig(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_1(self) -> UsageEvent:
        return UsageEvent(
            id=None,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_2(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=None,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_3(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=None,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_4(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=None,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_5(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=None,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_6(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=None,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_7(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=None,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_8(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=None,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_9(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=None,
        )

    def xǁUsageEventModelǁto_domain__mutmut_10(self) -> UsageEvent:
        return UsageEvent(
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_11(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_12(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_13(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_14(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_15(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_16(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            template=self.template,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_17(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            built_in_features=self.built_in_features,
        )

    def xǁUsageEventModelǁto_domain__mutmut_18(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            )

mutants_xǁUsageEventModelǁfrom_domain__mutmut['_mutmut_orig'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_1'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_2'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_3'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_4'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_5'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_6'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_7'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_8'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_9'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_10'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_11'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_12'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_13'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_14'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_15'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_16'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_17'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_18'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_19'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_20'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_21'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_22'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_23'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_23 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_24'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_24 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_25'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_25 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_26'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_26 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_27'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_27 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_28'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_28 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_29'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_29 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_30'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_30 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_31'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_31 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_32'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_32 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_33'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_33 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_34'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_34 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_35'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_35 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁfrom_domain__mutmut['xǁUsageEventModelǁfrom_domain__mutmut_36'] = UsageEventModel.xǁUsageEventModelǁfrom_domain__mutmut_36 # type: ignore # mutmut generated

mutants_xǁUsageEventModelǁto_domain__mutmut['_mutmut_orig'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_1'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_2'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_3'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_4'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_5'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_6'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_7'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_8'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_9'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_10'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_11'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_12'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_13'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_14'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_15'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_16'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_17'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUsageEventModelǁto_domain__mutmut['xǁUsageEventModelǁto_domain__mutmut_18'] = UsageEventModel.xǁUsageEventModelǁto_domain__mutmut_18 # type: ignore # mutmut generated
