# -*- coding: utf-8 -*-
""""""

from datetime import datetime

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, Float, Binary, Numeric
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker, scoped_session


Session = sessionmaker()


class Base(object):
    """Base mixin provides columns that shall be in all tables"""

    # Automatically set the tablename as per convention
    @declared_attr
    def __tablename__(cls):  # @NoSelf
        return cls.__name__.lower() + 's'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.now)
    modified = Column(DateTime, nullable=False, default=datetime.now)

DeclarativeBase = declarative_base(cls=Base)

metadata = DeclarativeBase.metadata

from noodle.core.model.share import Share, Host

__all__ = [
    'Session',
    'DeclarativeBase', 'metadata',
    'Share', 'Host',
    ]
