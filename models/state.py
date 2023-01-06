#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete"
    )
    
    @property
    def cities(self):
        from models import storage
        c = storage.all(Cities)
        my_cs = []
        for city in c.values():
            if c[state_id] == self.id:
                my_cs.append(city)

        return my_cs
        

