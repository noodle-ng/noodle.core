# -*- coding: utf-8 -*-
"""Development test script for the model"""

from noodle.core.model import Session, metadata, Share

if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    Session.configure(bind=engine)
    metadata.create_all(engine)  # @UndefinedVariable
    print Session().query(Share).all()
