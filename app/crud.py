from sqlalchemy.orm import Session
from . import models, schemas

def get_node(db: Session, node_id: int):
    return db.query(models.Node).filter(models.Node.id == node_id).first()

def create_node(db: Session, node: schemas.NodeCreate):
    db_node = models.Node(title=node.title, description=node.description)
    if node.parent_id:
        parent = get_node(db, node.parent_id)
        if parent:
            db_node.parents.append(parent)
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node

def update_node(db: Session, node_id: int, node: schemas.NodeUpdate):
    db_node = get_node(db, node_id)
    if db_node:
        db_node.title = node.title
        db_node.description = node.description
        db.commit()
        db.refresh(db_node)
    return db_node

def move_node(db: Session, node_id: int, new_parent_id: int):
    db_node = get_node(db, node_id)
    new_parent = get_node(db, new_parent_id)
    if db_node and new_parent and len(db_node.parents) == 1:
        db_node.parents = [new_parent]
        db.commit()
        db.refresh(db_node)
    return db_node

def link_node(db: Session, node_id: int, parent_id: int):
    db_node = get_node(db, node_id)
    parent = get_node(db, parent_id)
    if db_node and parent:
        db_node.parents.append(parent)
        db.commit()
        db.refresh(db_node)
    return db_node

def unlink_node(db: Session, node_id: int, parent_id: int):
    db_node = get_node(db, node_id)
    parent = get_node(db, parent_id)
    if db_node and parent and parent in db_node.parents:
        db_node.parents.remove(parent)
        db.commit()
        db.refresh(db_node)
    return db_node

def delete_node(db: Session, node_id: int):
    db_node = get_node(db, node_id)
    if db_node and len(db_node.parents) == 1:
        db.delete(db_node)
        db.commit()
        return True
    return False

def get_trajectory(db: Session, node_id: int):
    node = get_node(db, node_id)
    if not node:
        return []
    
    trajectory = [node]
    while node.parents:
        node = node.parents[0]  # Assuming single parent for simplicity
        trajectory.insert(0, node)
    
    return [n.id for n in trajectory]