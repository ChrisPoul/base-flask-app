from datetime import datetime
from dataclasses import dataclass
from sqlalchemy import (
    Column, String, DateTime
)
from . import database, Model


@dataclass
class User(database.Model, Model):
    """Some basic user class"""
    id: str = Column(
        String, default=Model.generate_unique_id, primary_key=True
    )
    name: str = Column(String(200), nullable=False, unique=False)
    joined_on: datetime = Column(DateTime, default=datetime.now)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    def get_id(self):
        return self.id
