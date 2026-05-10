# FastAPI Backend Tests

This directory contains automated tests for the FastAPI backend using the Arrange-Act-Assert (AAA) pattern and pytest.

## Running Tests

1. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Run tests:
   ```bash
   pytest
   ```

## Test Structure
- Each test follows the AAA pattern:
  - **Arrange:** Prepare test data and state
  - **Act:** Make the API call
  - **Assert:** Validate the response and side effects
