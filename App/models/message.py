from datetime import datetime
from sqlalchemy import (
    Column, String, DateTime
)
from sqlalchemy.sql import func
from . import database, Model


class Message(database.Model, Model):
    id: str = Column(
        String, primary_key=True, default=Model.generate_unique_id
    )
    contents: str = Column(String(100), nullable=False, unique=False)
    sent_at: datetime = Column(DateTime, server_default=func.now())
