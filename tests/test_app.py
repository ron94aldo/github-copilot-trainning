import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# --- Arrange-Act-Assert Pattern ---

def test_list_activities():
    # Arrange: (No setup needed, uses default in-memory data)
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    for activity in data.values():
        assert "description" in activity
        assert "participants" in activity
        assert "max_participants" in activity
        assert "schedule" in activity

def test_signup_for_activity():
    # Arrange
    activity_name = list(client.get("/activities").json().keys())[0]
    email = "testuser@example.com"
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert f"Signed up {email}" in data["message"]
    # Confirm participant is added
    participants = client.get("/activities").json()[activity_name]["participants"]
    assert email in participants

def test_signup_duplicate():
    # Arrange
    activity_name = list(client.get("/activities").json().keys())[0]
    email = "dupeuser@example.com"
    client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data["detail"]

def test_signup_invalid_activity():
    # Arrange
    activity_name = "nonexistent"
    email = "nouser@example.com"
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Activity not found"
