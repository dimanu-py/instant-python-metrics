import re
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, BeforeValidator, Field


def validate_uuid(value: str) -> str:
    try:
        UUID(value)
    except ValueError as error:
        raise ValueError(f"Invalid UUID: '{value}'. Expected a valid UUID v4 format.") from error
    return value


def validate_relaxed_semver(value: str) -> str:
    relaxed_semver_pattern = re.compile(r"^\d+\.\d+(\.\d+)?$")
    if not relaxed_semver_pattern.match(value):
        raise ValueError(f"Invalid Python version: '{value}'. Expected format X.Y or X.Y.Z (e.g., '3.11' or '3.11.5')")
    return value


def validate_strict_semver(value: str) -> str:
    strict_semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
    if not strict_semver_pattern.match(value):
        raise ValueError(f"Invalid semver: '{value}'. Expected format X.Y.Z (e.g., '1.2.3')")
    return value


def non_empty_feature(value: str) -> str:
    if value == "":
        raise ValueError("Feature name must be a non-empty string")
    return value


class UsageEventCreateRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    user_id: Annotated[str, BeforeValidator(validate_uuid)] = Field(min_length=1, max_length=256)
    ipy_version: Annotated[str, BeforeValidator(validate_strict_semver)] = Field(min_length=1, max_length=256)
    python_version: Annotated[str, BeforeValidator(validate_relaxed_semver)] = Field(min_length=1, max_length=256)
    operating_system: str = Field(min_length=1, max_length=256)
    command: str = Field(min_length=1, max_length=256)
    dependency_manager: str = Field(min_length=1, max_length=256)
    template: str = Field(min_length=1, max_length=256)
    built_in_features: list[Annotated[str, BeforeValidator(non_empty_feature)]] = Field(min_length=0)
