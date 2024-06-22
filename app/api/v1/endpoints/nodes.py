API Endpoints (nodes.py)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .... import crud, schemas
from ....database import get_db

router = APIRouter()

@router.post("/nodes/", response_model=schemas.Node)
def create_node(node: schemas.NodeCreate, db: Session = Depends(get_db)):
    return crud.create_node(db=db, node=node)

@router.get("/nodes/{node_id}", response_model=schemas.Node)
def read_node(node_id: int, db: Session = Depends(get_db)):
    db_node = crud.get_node(db, node_id=node_id)
    if db_node is None:
        raise HTTPException(status_code=404, detail="Node not found")
    return db_node

@router.put("/nodes/{node_id}", response_model=schemas.Node)
def update_node(node_id: int, node: schemas.NodeUpdate, db: Session = Depends(get_db)):
    db_node = crud.update_node(db, node_id=node_id, node=node)
    if db_node is None:
        raise HTTPException(status_code=404, detail="Node not found")
    return db_node

@router.put("/nodes/{node_id}/move/{new_parent_id}", response_model=schemas.Node)
def move_node(node_id: int, new_parent_id: int, db: Session = Depends(get_db)):
    db_node = crud.move_node(db, node_id=node_id, new_parent_id=new_parent_id)
    if db_node is None:
        raise HTTPException(status_code=404, detail="Node not found or cannot be moved")
    return db_node

@router.post("/nodes/{node_id}/link/{parent_id}", response_model=schemas.Node)
def link_node(node_id: int, parent_id: int, db: Session = Depends(get_db)):
    db_node = crud.link_node(db, node_id=node_id, parent_id=parent_id)
    if db_node is None:
        raise HTTPException(status_code=404, detail="Node or parent not found")
    return db_node

@router.delete("/nodes/{node_id}/unlink/{parent_id}", response_model=schemas.Node)
def unlink_node(node_id: int, parent_id: int, db: Session = Depends(get_db)):
    db_node = crud.unlink_node(db, node_id=node_id, parent_id=parent_id)
    if db_node is None:
        raise HTTPException(status_code=404, detail="Node or parent not found")
    return db_node

@router.delete("/nodes/{node_id}", response_model=bool)
def delete_node(node_id: int, db: Session = Depends(get_db)):
    success = crud.delete_node(db, node_id=node_id)
    if not success:
        raise HTTPException(status_code=404, detail="Node not found or cannot be deleted")
    return success

@router.get("/nodes/{node_id}/trajectory", response_model=List[int])
def get_node_trajectory(node_id: int, db: Session = Depends(get_db)):
    trajectory = crud.get_trajectory(db, node_id=node_id)
    if not trajectory:
        raise HTTPException(status_code=404, detail="Node not found")
    return trajectory
