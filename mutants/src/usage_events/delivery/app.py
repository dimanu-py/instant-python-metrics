"""FastAPI application factory for the usage events feature."""

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from usage_events.delivery.router import router
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


def create_app() -> FastAPI:
    args = []# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_create_app__mutmut_orig, x_create_app__mutmut_mutants, args, kwargs, None)


def x_create_app__mutmut_orig() -> FastAPI:
    app = FastAPI(title="Instant Python Metrics")
    app.include_router(router)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        """Handle validation errors, returning 400 for JSON decode errors."""
        errors = exc.errors()
        for error in errors:
            if error.get("type") == "json_invalid":
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Invalid JSON body"},
                )
        # For all other validation errors, use FastAPI's default format
        return JSONResponse(
            status_code=422,
            content=jsonable_encoder({"detail": exc.errors()}),
        )

    return app


def x_create_app__mutmut_1() -> FastAPI:
    app = None
    app.include_router(router)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        """Handle validation errors, returning 400 for JSON decode errors."""
        errors = exc.errors()
        for error in errors:
            if error.get("type") == "json_invalid":
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Invalid JSON body"},
                )
        # For all other validation errors, use FastAPI's default format
        return JSONResponse(
            status_code=422,
            content=jsonable_encoder({"detail": exc.errors()}),
        )

    return app


def x_create_app__mutmut_2() -> FastAPI:
    app = FastAPI(title=None)
    app.include_router(router)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        """Handle validation errors, returning 400 for JSON decode errors."""
        errors = exc.errors()
        for error in errors:
            if error.get("type") == "json_invalid":
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Invalid JSON body"},
                )
        # For all other validation errors, use FastAPI's default format
        return JSONResponse(
            status_code=422,
            content=jsonable_encoder({"detail": exc.errors()}),
        )

    return app


def x_create_app__mutmut_3() -> FastAPI:
    app = FastAPI(title="XXInstant Python MetricsXX")
    app.include_router(router)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        """Handle validation errors, returning 400 for JSON decode errors."""
        errors = exc.errors()
        for error in errors:
            if error.get("type") == "json_invalid":
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Invalid JSON body"},
                )
        # For all other validation errors, use FastAPI's default format
        return JSONResponse(
            status_code=422,
            content=jsonable_encoder({"detail": exc.errors()}),
        )

    return app


def x_create_app__mutmut_4() -> FastAPI:
    app = FastAPI(title="instant python metrics")
    app.include_router(router)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        """Handle validation errors, returning 400 for JSON decode errors."""
        errors = exc.errors()
        for error in errors:
            if error.get("type") == "json_invalid":
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Invalid JSON body"},
                )
        # For all other validation errors, use FastAPI's default format
        return JSONResponse(
            status_code=422,
            content=jsonable_encoder({"detail": exc.errors()}),
        )

    return app


def x_create_app__mutmut_5() -> FastAPI:
    app = FastAPI(title="INSTANT PYTHON METRICS")
    app.include_router(router)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        """Handle validation errors, returning 400 for JSON decode errors."""
        errors = exc.errors()
        for error in errors:
            if error.get("type") == "json_invalid":
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Invalid JSON body"},
                )
        # For all other validation errors, use FastAPI's default format
        return JSONResponse(
            status_code=422,
            content=jsonable_encoder({"detail": exc.errors()}),
        )

    return app


def x_create_app__mutmut_6() -> FastAPI:
    app = FastAPI(title="Instant Python Metrics")
    app.include_router(None)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        """Handle validation errors, returning 400 for JSON decode errors."""
        errors = exc.errors()
        for error in errors:
            if error.get("type") == "json_invalid":
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Invalid JSON body"},
                )
        # For all other validation errors, use FastAPI's default format
        return JSONResponse(
            status_code=422,
            content=jsonable_encoder({"detail": exc.errors()}),
        )

    return app

x_create_app__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_create_app__mutmut_1': x_create_app__mutmut_1, 
    'x_create_app__mutmut_2': x_create_app__mutmut_2, 
    'x_create_app__mutmut_3': x_create_app__mutmut_3, 
    'x_create_app__mutmut_4': x_create_app__mutmut_4, 
    'x_create_app__mutmut_5': x_create_app__mutmut_5, 
    'x_create_app__mutmut_6': x_create_app__mutmut_6
}
x_create_app__mutmut_orig.__name__ = 'x_create_app'
