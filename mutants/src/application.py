from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from common.errors.domain_error import DomainError
from common.http.error_response import InternalServerError, UnprocessableEntityError
from usage_events.routers import usage_events_router
from usage_events.session import create_database

app = FastAPI()

app.include_router(usage_events_router)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@app.on_event("startup")
def on_startup() -> None:
    create_database()


@app.exception_handler(Exception)
def unexpected_exception_handler(_: Request, __: Exception) -> JSONResponse:
    return InternalServerError().as_json()


@app.exception_handler(DomainError)
def domain_error_handler(_: Request, __: DomainError) -> JSONResponse:
    return UnprocessableEntityError().as_json()
