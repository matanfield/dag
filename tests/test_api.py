from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_node():
    response = client.post(
        "/api/v1/nodes/",
        json={"title": "Test Node", "description": "Test Description"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Node"
    assert data["description"] == "Test Description"

def test_read_node():
    # First, create a node
    create_response = client.post(
        "/api/v1/nodes/",
        json={"title": "Test Node", "description": "Test Description"},
    )
    node_id = create_response.json()["id"]

    # Then, read the node
    response = client.get(f"/api/v1/nodes/{node_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Node"
    assert data["description"] == "Test Description"

# Add more tests for update_node, move_node, link_node, unlink_node, delete_node API endpoints
