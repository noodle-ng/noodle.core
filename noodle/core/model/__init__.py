# -*- coding: utf-8 -*-
""""""

from datetime import datetime

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker, scoped_session


Session = sessionmaker()


class Base(object):
    """Base mixin provides columns that shall be in all tables"""

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.now)
    modified = Column(DateTime, nullable=False, default=datetime.now)

DeclarativeBase = declarative_base(cls=Base)

metadata = DeclarativeBase.metadata

from noodle.core.model.lib import IPAddress
from noodle.core.model.share import (
    Share, Content, Folderish,
    Folder, File,
    Service,
    Host,
    )

__all__ = [
    'Session',
    'IPAddress',
    'DeclarativeBase', 'metadata',
    'Share', 'Content', 'Folderish',
    'Folder', 'File',
    'Service',
    'Host',
    ]
