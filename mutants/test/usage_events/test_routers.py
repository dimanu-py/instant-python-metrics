import pytest
from doublex import Mock, expect_call
from doublex_expects import have_been_called_with
from expects import equal, expect
from fastapi.testclient import TestClient

from application import app
from test.usage_events.usage_event_mother import UsageEventMotherForPayload
from usage_events.routers import _get_usage_event_register
from usage_events.usage_event_register import UsageEventRegister


@pytest.mark.acceptance
class TestRegisterUsageEventAcceptance:
    def test_should_return_204_when_payload_is_valid(self, client: TestClient) -> None:
        payload = UsageEventMotherForPayload.dummy()

        response = client.post("/api/v1/events/", json=payload)

        expect(response.status_code).to(equal(204))

    def test_should_return_204_when_built_in_features_is_empty(self, client: TestClient) -> None:
        payload = UsageEventMotherForPayload.without_built_in_features_selected()

        response = client.post("/api/v1/events/", json=payload)

        expect(response.status_code).to(equal(204))

    def test_should_return_204_when_extra_unknown_fields_are_provided(self, client: TestClient) -> None:
        payload = UsageEventMotherForPayload.with_extra_unknown_fields()

        response = client.post("/api/v1/events/", json=payload)

        expect(response.status_code).to(equal(204))


@pytest.mark.unit
class TestRegisterUsageEventRouter:
    def test_should_return_204_when_payload_is_valid_and_forward_to_use_case(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        payload = UsageEventMotherForPayload.dummy()
        expect_call(register_mock).execute(**payload)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(204))
            expect(register_mock.execute).to(have_been_called_with(**payload))
        finally:
            app.dependency_overrides.clear()

    def test_should_return_422_when_required_field_is_missing(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            payload = UsageEventMotherForPayload.with_missing_field("ipy_version")
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(422))
        finally:
            app.dependency_overrides.clear()

    def test_should_return_422_when_field_is_empty_string(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            payload = {**UsageEventMotherForPayload.dummy(), "ipy_version": ""}
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(422))
        finally:
            app.dependency_overrides.clear()

    def test_should_return_422_when_ipy_version_is_invalid_semver(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            payload = {**UsageEventMotherForPayload.dummy(), "ipy_version": "1.2"}
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(422))
        finally:
            app.dependency_overrides.clear()

    def test_should_return_422_when_user_id_is_invalid_uuid(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            payload = {**UsageEventMotherForPayload.dummy(), "user_id": "not-a-valid-uuid"}
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(422))
        finally:
            app.dependency_overrides.clear()

    def test_should_return_422_when_built_in_features_is_not_array(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            payload = {**UsageEventMotherForPayload.dummy(), "built_in_features": "not-an-array"}
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(422))
        finally:
            app.dependency_overrides.clear()

    def test_should_return_422_when_built_in_features_has_empty_strings(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            payload = {**UsageEventMotherForPayload.dummy(), "built_in_features": ["tui", "", "formatting"]}
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(422))
        finally:
            app.dependency_overrides.clear()

    def test_should_return_422_when_json_body_is_malformed(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            response = client.post(
                "/api/v1/events/",
                content=b'{ "ipy_version": "1.2.3", , }',
                headers={"Content-Type": "application/json"},
            )
            expect(response.status_code).to(equal(422))
        finally:
            app.dependency_overrides.clear()

    def test_should_return_422_when_all_fields_are_empty(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            payload = {
                "ipy_version": "",
                "python_version": "",
                "operating_system": "",
                "user_id": "",
                "command": "",
                "dependency_manager": "",
                "template": "",
                "built_in_features": [],
            }
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(422))
        finally:
            app.dependency_overrides.clear()

    def test_should_return_422_when_mix_of_valid_and_invalid_fields(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            payload = {
                "ipy_version": "1.2.3",
                "python_version": "3",
                "operating_system": "Linux",
                "user_id": "not-a-uuid",
                "command": "init",
                "dependency_manager": "uv",
                "template": "default",
                "built_in_features": ["tui"],
            }
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(422))
        finally:
            app.dependency_overrides.clear()
