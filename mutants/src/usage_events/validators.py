import re
from uuid import UUID


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_non_empty_feature__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_non_empty_feature__mutmut)
def non_empty_feature(value: str) -> str:
    if value == "":
        raise ValueError("Feature name must be a non-empty string")
    return value


def x_non_empty_feature__mutmut_orig(value: str) -> str:
    if value == "":
        raise ValueError("Feature name must be a non-empty string")
    return value


def x_non_empty_feature__mutmut_1(value: str) -> str:
    if value != "":
        raise ValueError("Feature name must be a non-empty string")
    return value


def x_non_empty_feature__mutmut_2(value: str) -> str:
    if value == "XXXX":
        raise ValueError("Feature name must be a non-empty string")
    return value


def x_non_empty_feature__mutmut_3(value: str) -> str:
    if value == "":
        raise ValueError(None)
    return value


def x_non_empty_feature__mutmut_4(value: str) -> str:
    if value == "":
        raise ValueError("XXFeature name must be a non-empty stringXX")
    return value


def x_non_empty_feature__mutmut_5(value: str) -> str:
    if value == "":
        raise ValueError("feature name must be a non-empty string")
    return value


def x_non_empty_feature__mutmut_6(value: str) -> str:
    if value == "":
        raise ValueError("FEATURE NAME MUST BE A NON-EMPTY STRING")
    return value

mutants_x_non_empty_feature__mutmut['_mutmut_orig'] = x_non_empty_feature__mutmut_orig # type: ignore # mutmut generated
mutants_x_non_empty_feature__mutmut['x_non_empty_feature__mutmut_1'] = x_non_empty_feature__mutmut_1 # type: ignore # mutmut generated
mutants_x_non_empty_feature__mutmut['x_non_empty_feature__mutmut_2'] = x_non_empty_feature__mutmut_2 # type: ignore # mutmut generated
mutants_x_non_empty_feature__mutmut['x_non_empty_feature__mutmut_3'] = x_non_empty_feature__mutmut_3 # type: ignore # mutmut generated
mutants_x_non_empty_feature__mutmut['x_non_empty_feature__mutmut_4'] = x_non_empty_feature__mutmut_4 # type: ignore # mutmut generated
mutants_x_non_empty_feature__mutmut['x_non_empty_feature__mutmut_5'] = x_non_empty_feature__mutmut_5 # type: ignore # mutmut generated
mutants_x_non_empty_feature__mutmut['x_non_empty_feature__mutmut_6'] = x_non_empty_feature__mutmut_6 # type: ignore # mutmut generated
mutants_x_validate_strict_semver__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_validate_strict_semver__mutmut)
def validate_strict_semver(value: str) -> str:
    strict_semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
    if not strict_semver_pattern.match(value):
        raise ValueError(f"Invalid semver: '{value}'. Expected format X.Y.Z (e.g., '1.2.3')")
    return value


def x_validate_strict_semver__mutmut_orig(value: str) -> str:
    strict_semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
    if not strict_semver_pattern.match(value):
        raise ValueError(f"Invalid semver: '{value}'. Expected format X.Y.Z (e.g., '1.2.3')")
    return value


def x_validate_strict_semver__mutmut_1(value: str) -> str:
    strict_semver_pattern = None
    if not strict_semver_pattern.match(value):
        raise ValueError(f"Invalid semver: '{value}'. Expected format X.Y.Z (e.g., '1.2.3')")
    return value


def x_validate_strict_semver__mutmut_2(value: str) -> str:
    strict_semver_pattern = re.compile(None)
    if not strict_semver_pattern.match(value):
        raise ValueError(f"Invalid semver: '{value}'. Expected format X.Y.Z (e.g., '1.2.3')")
    return value


def x_validate_strict_semver__mutmut_3(value: str) -> str:
    strict_semver_pattern = re.compile(r"XX^\d+\.\d+\.\d+$XX")
    if not strict_semver_pattern.match(value):
        raise ValueError(f"Invalid semver: '{value}'. Expected format X.Y.Z (e.g., '1.2.3')")
    return value


def x_validate_strict_semver__mutmut_4(value: str) -> str:
    strict_semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
    if strict_semver_pattern.match(value):
        raise ValueError(f"Invalid semver: '{value}'. Expected format X.Y.Z (e.g., '1.2.3')")
    return value


def x_validate_strict_semver__mutmut_5(value: str) -> str:
    strict_semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
    if not strict_semver_pattern.match(None):
        raise ValueError(f"Invalid semver: '{value}'. Expected format X.Y.Z (e.g., '1.2.3')")
    return value


def x_validate_strict_semver__mutmut_6(value: str) -> str:
    strict_semver_pattern = re.compile(r"^\d+\.\d+\.\d+$")
    if not strict_semver_pattern.match(value):
        raise ValueError(None)
    return value

mutants_x_validate_strict_semver__mutmut['_mutmut_orig'] = x_validate_strict_semver__mutmut_orig # type: ignore # mutmut generated
mutants_x_validate_strict_semver__mutmut['x_validate_strict_semver__mutmut_1'] = x_validate_strict_semver__mutmut_1 # type: ignore # mutmut generated
mutants_x_validate_strict_semver__mutmut['x_validate_strict_semver__mutmut_2'] = x_validate_strict_semver__mutmut_2 # type: ignore # mutmut generated
mutants_x_validate_strict_semver__mutmut['x_validate_strict_semver__mutmut_3'] = x_validate_strict_semver__mutmut_3 # type: ignore # mutmut generated
mutants_x_validate_strict_semver__mutmut['x_validate_strict_semver__mutmut_4'] = x_validate_strict_semver__mutmut_4 # type: ignore # mutmut generated
mutants_x_validate_strict_semver__mutmut['x_validate_strict_semver__mutmut_5'] = x_validate_strict_semver__mutmut_5 # type: ignore # mutmut generated
mutants_x_validate_strict_semver__mutmut['x_validate_strict_semver__mutmut_6'] = x_validate_strict_semver__mutmut_6 # type: ignore # mutmut generated
mutants_x_validate_relaxed_semver__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_validate_relaxed_semver__mutmut)
def validate_relaxed_semver(value: str) -> str:
    relaxed_semver_pattern = re.compile(r"^\d+\.\d+(\.\d+)?$")
    if not relaxed_semver_pattern.match(value):
        raise ValueError(f"Invalid Python version: '{value}'. Expected format X.Y or X.Y.Z (e.g., '3.11' or '3.11.5')")
    return value


def x_validate_relaxed_semver__mutmut_orig(value: str) -> str:
    relaxed_semver_pattern = re.compile(r"^\d+\.\d+(\.\d+)?$")
    if not relaxed_semver_pattern.match(value):
        raise ValueError(f"Invalid Python version: '{value}'. Expected format X.Y or X.Y.Z (e.g., '3.11' or '3.11.5')")
    return value


def x_validate_relaxed_semver__mutmut_1(value: str) -> str:
    relaxed_semver_pattern = None
    if not relaxed_semver_pattern.match(value):
        raise ValueError(f"Invalid Python version: '{value}'. Expected format X.Y or X.Y.Z (e.g., '3.11' or '3.11.5')")
    return value


def x_validate_relaxed_semver__mutmut_2(value: str) -> str:
    relaxed_semver_pattern = re.compile(None)
    if not relaxed_semver_pattern.match(value):
        raise ValueError(f"Invalid Python version: '{value}'. Expected format X.Y or X.Y.Z (e.g., '3.11' or '3.11.5')")
    return value


def x_validate_relaxed_semver__mutmut_3(value: str) -> str:
    relaxed_semver_pattern = re.compile(r"XX^\d+\.\d+(\.\d+)?$XX")
    if not relaxed_semver_pattern.match(value):
        raise ValueError(f"Invalid Python version: '{value}'. Expected format X.Y or X.Y.Z (e.g., '3.11' or '3.11.5')")
    return value


def x_validate_relaxed_semver__mutmut_4(value: str) -> str:
    relaxed_semver_pattern = re.compile(r"^\d+\.\d+(\.\d+)?$")
    if relaxed_semver_pattern.match(value):
        raise ValueError(f"Invalid Python version: '{value}'. Expected format X.Y or X.Y.Z (e.g., '3.11' or '3.11.5')")
    return value


def x_validate_relaxed_semver__mutmut_5(value: str) -> str:
    relaxed_semver_pattern = re.compile(r"^\d+\.\d+(\.\d+)?$")
    if not relaxed_semver_pattern.match(None):
        raise ValueError(f"Invalid Python version: '{value}'. Expected format X.Y or X.Y.Z (e.g., '3.11' or '3.11.5')")
    return value


def x_validate_relaxed_semver__mutmut_6(value: str) -> str:
    relaxed_semver_pattern = re.compile(r"^\d+\.\d+(\.\d+)?$")
    if not relaxed_semver_pattern.match(value):
        raise ValueError(None)
    return value

mutants_x_validate_relaxed_semver__mutmut['_mutmut_orig'] = x_validate_relaxed_semver__mutmut_orig # type: ignore # mutmut generated
mutants_x_validate_relaxed_semver__mutmut['x_validate_relaxed_semver__mutmut_1'] = x_validate_relaxed_semver__mutmut_1 # type: ignore # mutmut generated
mutants_x_validate_relaxed_semver__mutmut['x_validate_relaxed_semver__mutmut_2'] = x_validate_relaxed_semver__mutmut_2 # type: ignore # mutmut generated
mutants_x_validate_relaxed_semver__mutmut['x_validate_relaxed_semver__mutmut_3'] = x_validate_relaxed_semver__mutmut_3 # type: ignore # mutmut generated
mutants_x_validate_relaxed_semver__mutmut['x_validate_relaxed_semver__mutmut_4'] = x_validate_relaxed_semver__mutmut_4 # type: ignore # mutmut generated
mutants_x_validate_relaxed_semver__mutmut['x_validate_relaxed_semver__mutmut_5'] = x_validate_relaxed_semver__mutmut_5 # type: ignore # mutmut generated
mutants_x_validate_relaxed_semver__mutmut['x_validate_relaxed_semver__mutmut_6'] = x_validate_relaxed_semver__mutmut_6 # type: ignore # mutmut generated
mutants_x_validate_uuid__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_validate_uuid__mutmut)
def validate_uuid(value: str) -> str:
    try:
        UUID(value)
    except ValueError as error:
        raise ValueError(f"Invalid UUID: '{value}'. Expected a valid UUID v4 format.") from error
    return value


def x_validate_uuid__mutmut_orig(value: str) -> str:
    try:
        UUID(value)
    except ValueError as error:
        raise ValueError(f"Invalid UUID: '{value}'. Expected a valid UUID v4 format.") from error
    return value


def x_validate_uuid__mutmut_1(value: str) -> str:
    try:
        UUID(None)
    except ValueError as error:
        raise ValueError(f"Invalid UUID: '{value}'. Expected a valid UUID v4 format.") from error
    return value


def x_validate_uuid__mutmut_2(value: str) -> str:
    try:
        UUID(value)
    except ValueError as error:
        raise ValueError(None) from error
    return value

mutants_x_validate_uuid__mutmut['_mutmut_orig'] = x_validate_uuid__mutmut_orig # type: ignore # mutmut generated
mutants_x_validate_uuid__mutmut['x_validate_uuid__mutmut_1'] = x_validate_uuid__mutmut_1 # type: ignore # mutmut generated
mutants_x_validate_uuid__mutmut['x_validate_uuid__mutmut_2'] = x_validate_uuid__mutmut_2 # type: ignore # mutmut generated
