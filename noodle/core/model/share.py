# -*- coding: utf-8 -*-
""""""

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, Unicode, DateTime, Float, Binary, Numeric, BigInteger

from noodle.core.model import DeclarativeBase


class Share(DeclarativeBase):
    parent_id = Column(Integer, ForeignKey('shares.id'))
    host_id = Column(Integer, ForeignKey('hosts.id'))

    name = Column(Unicode(256))

    type = Column(Unicode(20), nullable=False)
    __mapper_args__ = {'polymorphic_on': type}


#class Service(Share):
#    __mapper_args__ = {'polymorphic_identity': u'service'}


class Host(DeclarativeBase):
    name = Column(Unicode(256))
    #TODO: Custom column type wrapper
    ip = Column(BigInteger, nullable=False)

    sharesize = Column(BigInteger)

#    services = relationship(Service, backref='host')
#    statistics = relationship(Statistic, backref="host")
