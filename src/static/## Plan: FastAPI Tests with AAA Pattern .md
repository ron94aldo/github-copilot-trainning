## Plan: FastAPI Tests with AAA Pattern and Pytest

Automate backend testing using the Arrange-Act-Assert (AAA) pattern and `pytest` for test execution.

### Steps
1. Add `pytest` to `requirements.txt` for test dependency management.
2. Create a `tests/` directory at the project root.
3. Add `test_app.py` in `tests/` for backend API tests.
4. In `test_app.py`, set up FastAPI `TestClient` for the app.
5. Write tests for each endpoint using the AAA pattern:
    - **Arrange:** Prepare test data and state.
    - **Act:** Make the API call.
    - **Assert:** Validate the response and side effects.
6. Cover endpoints: activity listing, signup, and unregister (if implemented).
7. Add tests for error cases (e.g., duplicate signup, invalid activity).

### Further Considerations
1. Use fixtures or setup methods to reset in-memory data between tests.
2. Optionally, add a README in `tests/` explaining the AAA pattern and test execution.