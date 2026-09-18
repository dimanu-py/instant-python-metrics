Feature: Register Usage Event
  The CLI tool sends usage metrics to be validated and persisted in PostgreSQL.

  Background:
    Given the API endpoint is "POST /api/v1/events"

  @s1
  Scenario: Register a valid usage event with all required fields
    Given a payload:
      """
      {
        "ipy_version": "1.2.3",
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "550e8400-e29b-41d4-a716-446655440000",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": ["tui", "formatting"]
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 204

  @s2
  Scenario: Missing a required field returns 422
    Given a payload:
      """
      {
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "550e8400-e29b-41d4-a716-446655440000",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": ["tui"]
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 422
    And the response body should contain a validation error for field "ipy_version"

  @s3
  Scenario: An empty string field returns 422
    Given a payload:
      """
      {
        "ipy_version": "",
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "550e8400-e29b-41d4-a716-446655440000",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": ["tui"]
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 422
    And the response body should contain a validation error for field "ipy_version"

  @s4
  Scenario: Invalid ipy_version semver returns 422
    Given a payload:
      """
      {
        "ipy_version": "1.2",
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "550e8400-e29b-41d4-a716-446655440000",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": ["tui"]
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 422
    And the response body should contain a validation error for field "ipy_version"

  @s5
  Scenario: Invalid user_id UUID returns 422
    Given a payload:
      """
      {
        "ipy_version": "1.2.3",
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "not-a-valid-uuid",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": ["tui"]
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 422
    And the response body should contain a validation error for field "user_id"

  @s6
  Scenario: Non-array built_in_features returns 422
    Given a payload:
      """
      {
        "ipy_version": "1.2.3",
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "550e8400-e29b-41d4-a716-446655440000",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": "not-an-array"
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 422
    And the response body should contain a validation error for field "built_in_features"

  @s7
  Scenario: Empty strings inside built_in_features returns 422
    Given a payload:
      """
      {
        "ipy_version": "1.2.3",
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "550e8400-e29b-41d4-a716-446655440000",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": ["tui", "", "formatting"]
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 422
    And the response body should contain a validation error for the item at index 1 of "built_in_features"

  @s8
  Scenario: Empty built_in_features array is accepted
    Given a payload:
      """
      {
        "ipy_version": "1.2.3",
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "550e8400-e29b-41d4-a716-446655440000",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": []
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 204

  @s9
  Scenario: Extra unknown fields are silently ignored
    Given a payload:
      """
      {
        "ipy_version": "1.2.3",
        "python_version": "3.11",
        "operating_system": "Linux",
        "user_id": "550e8400-e29b-41d4-a716-446655440000",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": ["tui"],
        "unknown_field": "should be ignored",
        "another_unknown": 42
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 204

  @s10
  Scenario: Malformed JSON body returns 422
    Given a malformed request body:
      """
      { "ipy_version": "1.2.3", , }
      """
    When the client sends a POST request with the malformed body
    Then the response status should be 422

  @s11
  Scenario: All fields empty returns 422 with errors for every field
    Given a payload:
      """
      {
        "ipy_version": "",
        "python_version": "",
        "operating_system": "",
        "user_id": "",
        "command": "",
        "dependency_manager": "",
        "template": "",
        "built_in_features": []
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 422
    And the response body should contain validation errors for all 8 fields

  @s12
  Scenario: Mix of valid and invalid fields returns 422 for invalid fields only
    Given a payload:
      """
      {
        "ipy_version": "1.2.3",
        "python_version": "3",
        "operating_system": "Linux",
        "user_id": "not-a-uuid",
        "command": "init",
        "dependency_manager": "uv",
        "template": "default",
        "built_in_features": ["tui"]
      }
      """
    When the client sends a POST request with the payload
    Then the response status should be 422
    And the response body should contain a validation error for field "python_version"
    And the response body should contain a validation error for field "user_id"
    And the response body should NOT contain a validation error for field "ipy_version"
    And the response body should NOT contain a validation error for field "command"
