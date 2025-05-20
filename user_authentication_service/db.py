#!/usr/bin/env python3
"""
DB module for managing database connection and user operations.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound  
from sqlalchemy.exc import InvalidRequestError


from user import Base, User


class DB:
    """
    DB class for managing user operations with SQLAlchemy.
    """

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the database"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds the first user that matches the given keyword arguments.

        Raises:
            InvalidRequestError: If query is invalid.
            NoResultFound: If no user matches.
        """
        if not kwargs:
            raise InvalidRequestError("No arguments provided")

        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found matching the criteria")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments")
