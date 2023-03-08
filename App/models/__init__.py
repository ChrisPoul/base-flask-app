import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Query

database = SQLAlchemy()


class Model:
    query: Query

    def add(self):
        database.session.add(self)
        self.save()

    def update(self, **kwargs):
        for attr in kwargs:
            setattr(self, attr, kwargs[attr])
        self.save()

    def save(self):
        database.session.commit()

    def delete(self):
        database.session.delete(self)
        self.save()

    @staticmethod
    def generate_unique_id() -> str:
        return uuid.uuid4().hex
