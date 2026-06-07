Feature: Register Usage Event

  As a user of the instant-python CLI
  I want the CLI to register a usage event each time I execute a command
  So that the project maintainers can understand usage patterns

  Background:
    Given the API server is running
    And the PostgreSQL database is available

  Scenario: Register a valid usage event with all fields
    Given a valid usage event payload:
      | Field              | Value                                    |
      | ipy_version        | 1.2.3                                    |
      | operating_system   | linux                                    |
      | distinct_id        | a1b2c3d4-e5f6-4789-abcd-ef1234567890     |
      | command            | generate                                 |
      | python_version     | 3.13.1                                   |
      | dependency_manager | uv                                       |
      | template           | standard_project                         |
      | built_in_features  | ["github_actions"]                       |
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 201 Created response
    And the response body contains an "id" field with a UUID value
    And the Location header points to /api/v1/events/{id}

  Scenario: Missing a required field returns 422
    Given a payload missing the "ipy_version" field
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 422 Unprocessable Entity response
    And the response body contains a validation error for the "ipy_version" field

  Scenario: Multiple missing required fields returns 422 with all errors
    Given a payload missing the "command", "template", and "distinct_id" fields
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 422 Unprocessable Entity response
    And the response body contains validation errors for each missing field

  Scenario: Empty distinct_id is rejected
    Given a payload with an empty string as "distinct_id"
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 422 Unprocessable Entity response

  Scenario: Invalid distinct_id format is rejected
    Given a payload with "distinct_id" set to "not-a-uuid"
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 422 Unprocessable Entity response

  Scenario: Malformed semver in ipy_version is rejected
    Given a payload with "ipy_version" set to "not-a-version"
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 422 Unprocessable Entity response

  Scenario: Empty categorical field is rejected
    Given a payload with an empty string as "command"
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 422 Unprocessable Entity response

  Scenario: Field exceeding max length is rejected
    Given a payload with "template" set to a 256-character string
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 422 Unprocessable Entity response

  Scenario: Malformed JSON body returns 400
    Given an invalid JSON body (e.g., trailing comma)
    When the CLI sends a POST request to /api/v1/events with the body
    Then the API returns a 400 Bad Request response

  Scenario: Empty built_in_features list is accepted
    Given a valid payload with an empty list as "built_in_features"
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 201 Created response

  Scenario: Extra unknown fields are silently ignored
    Given a valid payload with an additional "unexpected_field" field
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 201 Created response

  Scenario: Database unavailable returns 503
    Given the API server is running but the database is unavailable
    And a valid usage event payload
    When the CLI sends a POST request to /api/v1/events with the payload
    Then the API returns a 503 Service Unavailable response
