"""FastAPI application factory for the usage events feature."""

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from usage_events.delivery.router import router


def create_app() -> FastAPI:
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
