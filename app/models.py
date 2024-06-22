from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

node_parent = Table('node_parent', Base.metadata,
    Column('node_id', Integer, ForeignKey('nodes.id'), primary_key=True),
    Column('parent_id', Integer, ForeignKey('nodes.id'), primary_key=True)
)

class Node(Base):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    
    parents = relationship(
        'Node', 
        secondary=node_parent,
        primaryjoin=(node_parent.c.node_id == id),
        secondaryjoin=(node_parent.c.parent_id == id),
        backref='children'
    )

    def __repr__(self):
        return f"<Node(id={self.id}, title='{self.title}')>"