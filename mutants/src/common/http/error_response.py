from abc import ABC

from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁErrorResponseǁas_json__mutmut: MutantDict = {}  # type: ignore


class ErrorResponse(ABC, BaseModel):
    status_code: int
    detail: str

    @_mutmut_mutated(mutants_xǁErrorResponseǁas_json__mutmut)
    def as_json(self) -> JSONResponse:
        return JSONResponse(
            content={"detail": self.detail},
            status_code=self.status_code,
        )

    def xǁErrorResponseǁas_json__mutmut_orig(self) -> JSONResponse:
        return JSONResponse(
            content={"detail": self.detail},
            status_code=self.status_code,
        )

    def xǁErrorResponseǁas_json__mutmut_1(self) -> JSONResponse:
        return JSONResponse(
            content=None,
            status_code=self.status_code,
        )

    def xǁErrorResponseǁas_json__mutmut_2(self) -> JSONResponse:
        return JSONResponse(
            content={"detail": self.detail},
            status_code=None,
        )

    def xǁErrorResponseǁas_json__mutmut_3(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.status_code,
        )

    def xǁErrorResponseǁas_json__mutmut_4(self) -> JSONResponse:
        return JSONResponse(
            content={"detail": self.detail},
            )

    def xǁErrorResponseǁas_json__mutmut_5(self) -> JSONResponse:
        return JSONResponse(
            content={"XXdetailXX": self.detail},
            status_code=self.status_code,
        )

    def xǁErrorResponseǁas_json__mutmut_6(self) -> JSONResponse:
        return JSONResponse(
            content={"DETAIL": self.detail},
            status_code=self.status_code,
        )

mutants_xǁErrorResponseǁas_json__mutmut['_mutmut_orig'] = ErrorResponse.xǁErrorResponseǁas_json__mutmut_orig # type: ignore # mutmut generated
mutants_xǁErrorResponseǁas_json__mutmut['xǁErrorResponseǁas_json__mutmut_1'] = ErrorResponse.xǁErrorResponseǁas_json__mutmut_1 # type: ignore # mutmut generated
mutants_xǁErrorResponseǁas_json__mutmut['xǁErrorResponseǁas_json__mutmut_2'] = ErrorResponse.xǁErrorResponseǁas_json__mutmut_2 # type: ignore # mutmut generated
mutants_xǁErrorResponseǁas_json__mutmut['xǁErrorResponseǁas_json__mutmut_3'] = ErrorResponse.xǁErrorResponseǁas_json__mutmut_3 # type: ignore # mutmut generated
mutants_xǁErrorResponseǁas_json__mutmut['xǁErrorResponseǁas_json__mutmut_4'] = ErrorResponse.xǁErrorResponseǁas_json__mutmut_4 # type: ignore # mutmut generated
mutants_xǁErrorResponseǁas_json__mutmut['xǁErrorResponseǁas_json__mutmut_5'] = ErrorResponse.xǁErrorResponseǁas_json__mutmut_5 # type: ignore # mutmut generated
mutants_xǁErrorResponseǁas_json__mutmut['xǁErrorResponseǁas_json__mutmut_6'] = ErrorResponse.xǁErrorResponseǁas_json__mutmut_6 # type: ignore # mutmut generated


class UnprocessableEntityError(ErrorResponse):
    status_code: int = Field(default=status.HTTP_422_UNPROCESSABLE_CONTENT)
    detail: str = Field(default="Unprocessable Entity")


class ResourceNotFoundError(ErrorResponse):
    status_code: int = Field(default=status.HTTP_404_NOT_FOUND)
    detail: str = Field(default="Not Found")


class InternalServerError(ErrorResponse):
    status_code: int = Field(default=status.HTTP_500_INTERNAL_SERVER_ERROR)
    detail: str = Field(default="An unexpected error occurred.")
