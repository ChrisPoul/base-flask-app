import uuid
from typing import Union
from typing_extensions import Self
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Query

database = SQLAlchemy()


class Model:
    query: Query

    def add(self):
        """
        Add this instance to the database
        """
        database.session.add(self)
        self.save()

    def update(self, **kwargs):
        for attr in kwargs:
            setattr(self, attr, kwargs[attr])
        self.save()

    def save(self):
        """Save any changes to the database"""
        database.session.commit()

    def delete(self):
        database.session.delete(self)
        self.save()

    @staticmethod
    def generate_unique_id() -> str:
        return uuid.uuid4().hex

    @classmethod
    def get(cls, id: str) -> Union[Self, None]:
        """Return an instance based on the given primary key identifier, or None if not found.
        E.g.:
        my_user = User.get("unique_id")
        """
        if id is None:
            return None

        return cls.query.get(id)

    @classmethod
    def all(cls) -> 'list[Self]':
        """
        Return a list of all instances of the given Model
        """
        return cls.query.all()

    @classmethod
    def get_by(cls, **kwargs) -> Union[Self, None]:
        """
        Apply the given filtering criterion using keyword expressions.
        e.g.::
            MyClass.get_by(name='some name')
        :return: The first object that passes the filtering criterion
        """
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_all_by(cls, **kwargs) -> 'list[Self]':
        """
        Apply the given filtering criterion using keyword expressions.
        e.g.::
            MyClass.get_all_by(name='some name')
        Multiple criteria may be specified as comma separated; the effect
        is that they will be joined together using the :func:`.and_`
        function::
            MyClass.get_all_by(name='some name', id=5)
        :return: List of objects that pass the filtering criterion
        """
        return cls.query.filter_by(**kwargs).all()
