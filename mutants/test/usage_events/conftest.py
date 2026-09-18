from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from testcontainers.postgres import PostgresContainer

from application import app
from usage_events.session import reconfigure


@pytest.fixture(scope="session")
def postgres_container() -> Generator[PostgresContainer]:
    with PostgresContainer("postgres:16-alpine") as pg:
        yield pg


@pytest.fixture
def client(postgres_container: PostgresContainer) -> Generator[TestClient]:
    from usage_events.session import create_database

    reconfigure(postgres_container.get_connection_url())
    create_database()

    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
