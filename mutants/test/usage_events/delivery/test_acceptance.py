"""Acceptance tests for the Register Usage Event feature."""

from uuid import UUID

import pytest
from expects import equal, expect, have_key
from fastapi.testclient import TestClient


@pytest.mark.acceptance
class TestRegisterUsageEvent:
    """Acceptance tests for POST /api/v1/events."""

    def test_valid_usage_event_returns_201_with_id_and_location(self, client: TestClient) -> None:
        """@s1: Register a valid usage event with all fields."""
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

        expect(response.status_code).to(equal(201))
        data = response.json()
        expect(data).to(have_key("id"))
        # Verify it's a valid UUID v7
        uuid_obj = UUID(data["id"])
        expect(uuid_obj.version).to(equal(7))
        expect(response.headers).to(have_key("location"))
        expect(response.headers["location"]).to(equal(f"/api/v1/events/{data['id']}"))
