# -*- coding: utf-8 -*-
"""Development test script for the model"""

from noodle.core.model import *  # @UnusedWildImport

if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    Session.configure(bind=engine)
    metadata.create_all(engine)  # @UndefinedVariable
    print Session().query(Share).all()
    print dir(Share)
    print dir(Folder)
    print dir(File)
    print dir(Service)
