# -*- coding: utf-8 -*-
""""""

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Integer, Unicode, DateTime, Float, Binary, Numeric, BigInteger, Enum

from noodle.core.model import DeclarativeBase, IPAddress


class Share(DeclarativeBase):
    '''Polymorphic base class for Share objects'''
    __tablename__ = 'shares'

    parent_id = Column(Integer, ForeignKey('shares.id'))

    name = Column(Unicode(256))

    type = Column(
        Enum(u'folderish', u'content', u'folder', u'file', u'service',
            name='share_type'),
        nullable=False)

    __mapper_args__ = {'polymorphic_on': type}


class Folderish(Share):
    '''Polymorphic mixin for entities with children'''

    children = relationship(Share, cascade='all',
        backref=backref('parent', remote_side='Share.id'))

    __mapper_args__ = {'polymorphic_identity': u'folderish'}


class Content(Share):
    '''Polymorphic mixin for entities with a size'''

    size = Column(BigInteger)

    __mapper_args__ = {'polymorphic_identity': u'content'}


class Folder(Content, Folderish):
    '''Folder'''

    __mapper_args__ = {'polymorphic_identity': u'folder'}


class File(Content):
    '''File'''

    extension = Column(Unicode(256))

    hash = Column(Unicode(256))

    __mapper_args__ = {'polymorphic_identity': u'file'}


class Service(Content, Folderish):
    '''Service is the most top-level Share object'''

    host_id = Column(Integer, ForeignKey('hosts.id'))

    host = relationship('Host', backref=backref('services'))

    __mapper_args__ = {'polymorphic_identity': u'service'}


class Host(DeclarativeBase):
    '''Host'''
    __tablename__ = u'hosts'

    name = Column(Unicode(256))

    ip = Column(IPAddress, nullable=False)

    sharesize = Column(BigInteger)

#    services = relationship(Service, backref='host')
