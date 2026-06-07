"""Delivery unit tests for the usage events router."""

from __future__ import annotations

import pytest
from expects import equal, expect, have_key
from fastapi.testclient import TestClient


@pytest.mark.unit
class TestRegisterUsageEventRouter:
    """Unit tests for POST /api/v1/events router."""

    def test_missing_required_field_returns_422(self, client: TestClient) -> None:
        """@s2: Missing a required field returns 422."""
        payload = {
            "operating_system": "linux",
            "distinct_id": "a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            "command": "generate",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "template": "standard_project",
            "built_in_features": ["github_actions"],
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(422))
        data = response.json()
        expect(data).to(have_key("detail"))

    def test_multiple_missing_fields_returns_422_for_each(self, client: TestClient) -> None:
        """@s3: Multiple missing required fields returns 422 with all errors."""
        payload = {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "built_in_features": ["github_actions"],
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(422))
        data = response.json()
        expect(data).to(have_key("detail"))
        missing_fields = {err["loc"][-1] for err in data["detail"]}
        expect("command" in missing_fields).to(equal(True))
        expect("template" in missing_fields).to(equal(True))
        expect("distinct_id" in missing_fields).to(equal(True))

    def test_invalid_distinct_id_format_is_rejected(self, client: TestClient) -> None:
        """@s5: Invalid distinct_id format is rejected."""
        payload = {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "distinct_id": "not-a-uuid",
            "command": "generate",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "template": "standard_project",
            "built_in_features": ["github_actions"],
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(422))

    def test_malformed_semver_in_ipy_version_is_rejected(self, client: TestClient) -> None:
        """@s6: Malformed semver in ipy_version is rejected."""
        payload = {
            "ipy_version": "not-a-version",
            "operating_system": "linux",
            "distinct_id": "a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            "command": "generate",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "template": "standard_project",
            "built_in_features": ["github_actions"],
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(422))

    def test_extra_unknown_fields_are_silently_ignored(self, client: TestClient) -> None:
        """@s11: Extra unknown fields are silently ignored."""
        payload = {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "distinct_id": "a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            "command": "generate",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "template": "standard_project",
            "built_in_features": ["github_actions"],
            "unexpected_field": "should be ignored",
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(201))

    def test_empty_built_in_features_list_is_accepted(self, client: TestClient) -> None:
        """@s10: Empty built_in_features list is accepted."""
        payload = {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "distinct_id": "a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            "command": "generate",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "template": "standard_project",
            "built_in_features": [],
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(201))

    def test_database_unavailable_returns_503(self, client: TestClient) -> None:
        """@s12: Database unavailable returns 503."""
        from doublex import ANY_ARG, Mock, expect_call

        from usage_events.delivery.router import _get_repository
        from usage_events.domain.usage_event_repository import UsageEventRepository

        repository = Mock(UsageEventRepository)
        expect_call(repository).save(ANY_ARG).raises(RuntimeError("Database connection failed"))

        # Inject failing repository via FastAPI dependency override
        client.app.dependency_overrides[_get_repository] = lambda: repository  # type: ignore[attr-defined]

        payload = {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "distinct_id": "a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            "command": "generate",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "template": "standard_project",
            "built_in_features": ["github_actions"],
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(503))

        # Clean up
        client.app.dependency_overrides.clear()  # type: ignore[attr-defined]

    def test_malformed_json_body_returns_400(self, client: TestClient) -> None:
        """@s9: Malformed JSON body returns 400."""
        response = client.post(
            "/api/v1/events",
            content=b"{malformed json}",
            headers={"content-type": "application/json"},
        )

        expect(response.status_code).to(equal(400))

    def test_field_exceeding_max_length_is_rejected(self, client: TestClient) -> None:
        """@s8: Field exceeding max length is rejected."""
        long_string = "a" * 256
        payload = {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "distinct_id": "a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            "command": "generate",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "template": long_string,
            "built_in_features": ["github_actions"],
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(422))

    def test_empty_categorical_field_is_rejected(self, client: TestClient) -> None:
        """@s7: Empty categorical field is rejected."""
        payload = {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "distinct_id": "a1b2c3d4-e5f6-4789-abcd-ef1234567890",
            "command": "",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "template": "standard_project",
            "built_in_features": ["github_actions"],
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(422))

    def test_empty_distinct_id_is_rejected(self, client: TestClient) -> None:
        """@s4: Empty distinct_id is rejected."""
        payload = {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "distinct_id": "",
            "command": "generate",
            "python_version": "3.13.1",
            "dependency_manager": "uv",
            "template": "standard_project",
            "built_in_features": ["github_actions"],
        }

        response = client.post("/api/v1/events", json=payload)

        expect(response.status_code).to(equal(422))
