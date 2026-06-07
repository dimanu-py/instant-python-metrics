"""Shared fixtures for all tests."""

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from usage_events.delivery.app import create_app


@pytest.fixture(name="client")
def client_fixture() -> Generator[TestClient]:
    """Create a TestClient for the FastAPI application."""
    app = create_app()
    with TestClient(app) as client:
        yield client
