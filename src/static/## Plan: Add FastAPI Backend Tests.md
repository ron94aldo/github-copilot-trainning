## Plan: Add FastAPI Backend Tests

Add a `tests/` directory with automated tests for the FastAPI backend to ensure endpoints work as expected.

### Steps
1. Create a `tests/` directory at the project root.
2. Add `test_app.py` in `tests/` for backend API tests.
3. Set up FastAPI `TestClient` in `tests/test_app.py`.
4. Write tests for activity listing, signup, and (if implemented) unregister endpoints.
5. Update `pytest.ini` if needed to include the new test path.

### Further Considerations
1. Should tests use in-memory data or fixtures for isolation?
2. Consider adding tests for error cases (e.g., duplicate signup, invalid activity).
3. Optionally add a requirements section for test dependencies (e.g., `pytest`, `httpx`).