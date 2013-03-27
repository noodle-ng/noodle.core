# -*- coding: utf-8 -*-
"""Development test script for the model"""

from time import sleep

from noodle.core.model import *  # @UnusedWildImport


url = 'sqlite:///:memory:'


if __name__ == '__main__':
#    print dir(Share)
#    print dir(Folder)
#    print dir(File)
#    print dir(Service)


    from sqlalchemy import create_engine
    engine = create_engine(url, echo=True)
    Session.configure(bind=engine)
    metadata.create_all(engine)  # @UndefinedVariable

    s = Session()
    print s.query(Share).all()

    s = Session()
    h = Host(ip='1.2.3.4', name='endoftheinternet')
    s.add(h)
    s.commit()

    s = Session()
    h = s.query(Host).first()
    print h, h.ip, h.name, h.created, h.modified

    sleep(1)

    s = Session()
    h = s.query(Host).first()
    h.ip = '192.168.0.1'
    h.name = 'beginoftheinternet'
    s.add(h)
    s.commit()

    s = Session()
    h = s.query(Host).first()
    print h, h.ip, h.name, h.created, h.modified
