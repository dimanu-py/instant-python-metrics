from collections.abc import Generator

import pytest
from expects import equal, expect
from sqlalchemy import select
from testcontainers.postgres import PostgresContainer

from test.usage_events.usage_event_mother import UsageEventMother
from usage_events.session import SessionManager
from usage_events.usage_event import UsageEvent
from usage_events.usage_event_model import UsageEventModel
from usage_events.usage_event_repository import PostgresUsageEventRepository


@pytest.mark.integration
class TestUsageEventRepository:
    @pytest.fixture(scope="class")
    def session_manager(self) -> Generator[SessionManager]:
        with PostgresContainer("postgres:16-alpine") as postgres:
            manager = SessionManager(postgres.get_connection_url())
            manager.create_tables()
            yield manager

    @pytest.fixture(autouse=True)
    def clean_database(self, session_manager: SessionManager) -> Generator[None]:
        yield
        session_manager.clean_tables()

    def test_should_save_usage_event_with_all_fields_preserved(self, session_manager: SessionManager) -> None:
        expected = UsageEventMother.with_id("06a2e698-4377-7f43-8000-0a4f8c034fd4")

        with session_manager.session() as session:
            repository = PostgresUsageEventRepository(session=session)
            repository.save(expected)

        with session_manager.session() as session:
            rows = list(session.execute(select(UsageEventModel)).scalars())

        expect(len(rows)).to(equal(1))
        actual = rows[0]
        expect(actual.id).to(equal(expected["id"]))
        expect(actual.user_id).to(equal(expected["user_id"]))
        expect(actual.ipy_version).to(equal(expected["ipy_version"]))
        expect(actual.python_version).to(equal(expected["python_version"]))
        expect(actual.operating_system).to(equal(expected["operating_system"]))
        expect(actual.command).to(equal(expected["command"]))
        expect(actual.dependency_manager).to(equal(expected["dependency_manager"]))
        expect(actual.template).to(equal(expected["template"]))
        expect(actual.built_in_features).to(equal(expected["built_in_features"]))
        expect(actual.created_at).not_to(equal(None))

    def test_should_roundtrip_via_from_domain_and_to_domain(self, session_manager: SessionManager) -> None:
        expected = UsageEventMother.with_id("06a2e698-4377-7f43-8000-0a4f8c034fd5")

        with session_manager.session() as session:
            repository = PostgresUsageEventRepository(session=session)
            repository.save(expected)

        with session_manager.session() as session:
            rows = list(session.execute(select(UsageEventModel)).scalars())

        roundtripped: UsageEvent = rows[0].to_domain()

        expect(roundtripped["id"]).to(equal(expected["id"]))
        expect(roundtripped["user_id"]).to(equal(expected["user_id"]))
        expect(roundtripped["ipy_version"]).to(equal(expected["ipy_version"]))
        expect(roundtripped["python_version"]).to(equal(expected["python_version"]))
        expect(roundtripped["operating_system"]).to(equal(expected["operating_system"]))
        expect(roundtripped["command"]).to(equal(expected["command"]))
        expect(roundtripped["dependency_manager"]).to(equal(expected["dependency_manager"]))
        expect(roundtripped["template"]).to(equal(expected["template"]))
        expect(roundtripped["built_in_features"]).to(equal(expected["built_in_features"]))

    def test_should_save_multiple_usage_events_with_different_ids(self, session_manager: SessionManager) -> None:
        first = UsageEventMother.with_id("06a2e698-4377-7f43-8000-0a4f8c034fd6")
        second = UsageEventMother.with_id("06a2e698-4377-7f43-8000-0a4f8c034fd7")

        with session_manager.session() as session:
            repository = PostgresUsageEventRepository(session=session)
            repository.save(first)
            repository.save(second)

        with session_manager.session() as session:
            rows = list(session.execute(select(UsageEventModel)).scalars())

        expect(len(rows)).to(equal(2))


