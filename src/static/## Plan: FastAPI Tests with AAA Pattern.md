## Plan: FastAPI Tests with AAA Pattern

Automate backend testing using the Arrange-Act-Assert (AAA) pattern for clarity and maintainability.

### Steps
1. Create a `tests/` directory at the project root.
2. Add `test_app.py` in `tests/` for backend API tests.
3. In `test_app.py`, set up FastAPI `TestClient` for the app.
4. For each endpoint, write tests using the AAA pattern:
    - **Arrange:** Set up test data and state.
    - **Act:** Make the API call.
    - **Assert:** Check the response and side effects.
5. Cover endpoints: activity listing, signup, and unregister (if implemented).
6. Add tests for error cases (e.g., duplicate signup, invalid activity).

### Further Considerations
1. Use fixtures or setup methods to reset in-memory data between tests.
2. Ensure test dependencies (`pytest`, `httpx`, `fastapi`) are listed in `requirements.txt` or a test requirements file.
3. Optionally, add a README in `tests/` explaining the AAA pattern usage.