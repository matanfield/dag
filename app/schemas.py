from pydantic import BaseModel
from typing import List, Optional

class NodeBase(BaseModel):
    title: str
    description: str

class NodeCreate(NodeBase):
    parent_id: Optional[int] = None

class NodeUpdate(NodeBase):
    pass

class Node(NodeBase):
    id: int
    parent_ids: List[int]
    child_ids: List[int]
    trajectory: List[int]

    class Config:
        orm_mode = True
