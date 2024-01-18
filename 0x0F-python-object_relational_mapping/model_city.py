#!/usr/bin/python3
"""SQLAlchemy"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """City class"""

    __tablename__ = "cities"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(
        "state_id",
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
    