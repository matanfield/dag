import pytest
from sqlalchemy.orm import Session
from app import crud, models, schemas

def test_create_node(db: Session):
    node = schemas.NodeCreate(title="Test Node", description="Test Description")
    db_node = crud.create_node(db, node)
    assert db_node.title == "Test Node"
    assert db_node.description == "Test Description"

def test_get_node(db: Session):
    node = crud.create_node(db, schemas.NodeCreate(title="Test Node", description="Test Description"))
    retrieved_node = crud.get_node(db, node.id)
    assert retrieved_node.id == node.id
    assert retrieved_node.title == node.title

# Add more tests for update_node, move_node, link_node, unlink_node, delete_node, etc.