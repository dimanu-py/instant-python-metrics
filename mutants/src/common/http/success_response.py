from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette import status


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSuccessResponseǁas_json__mutmut: MutantDict = {}  # type: ignore


class SuccessResponse(BaseModel):
    status_code: int
    data: dict

    @_mutmut_mutated(mutants_xǁSuccessResponseǁas_json__mutmut)
    def as_json(self) -> JSONResponse:
        return JSONResponse(
            content=self.data,
            status_code=self.status_code,
        )

    def xǁSuccessResponseǁas_json__mutmut_orig(self) -> JSONResponse:
        return JSONResponse(
            content=self.data,
            status_code=self.status_code,
        )

    def xǁSuccessResponseǁas_json__mutmut_1(self) -> JSONResponse:
        return JSONResponse(
            content=None,
            status_code=self.status_code,
        )

    def xǁSuccessResponseǁas_json__mutmut_2(self) -> JSONResponse:
        return JSONResponse(
            content=self.data,
            status_code=None,
        )

    def xǁSuccessResponseǁas_json__mutmut_3(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.status_code,
        )

    def xǁSuccessResponseǁas_json__mutmut_4(self) -> JSONResponse:
        return JSONResponse(
            content=self.data,
            )

mutants_xǁSuccessResponseǁas_json__mutmut['_mutmut_orig'] = SuccessResponse.xǁSuccessResponseǁas_json__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSuccessResponseǁas_json__mutmut['xǁSuccessResponseǁas_json__mutmut_1'] = SuccessResponse.xǁSuccessResponseǁas_json__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSuccessResponseǁas_json__mutmut['xǁSuccessResponseǁas_json__mutmut_2'] = SuccessResponse.xǁSuccessResponseǁas_json__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSuccessResponseǁas_json__mutmut['xǁSuccessResponseǁas_json__mutmut_3'] = SuccessResponse.xǁSuccessResponseǁas_json__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSuccessResponseǁas_json__mutmut['xǁSuccessResponseǁas_json__mutmut_4'] = SuccessResponse.xǁSuccessResponseǁas_json__mutmut_4 # type: ignore # mutmut generated


class NoContentResponse(SuccessResponse):
    status_code: int = status.HTTP_204_NO_CONTENT
    data: dict = {}
