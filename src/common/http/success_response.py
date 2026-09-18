from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette import status


class SuccessResponse(BaseModel):
    status_code: int
    data: dict

    def as_json(self) -> JSONResponse:
        return JSONResponse(
            content=self.data,
            status_code=self.status_code,
        )


class NoContentResponse(SuccessResponse):
    status_code: int = status.HTTP_204_NO_CONTENT
    data: dict = {}
