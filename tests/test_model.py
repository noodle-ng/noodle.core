# -*- coding: utf-8 -*-

import unittest

from sqlalchemy import create_engine


class TestModel(unittest.TestCase):
    '''Test the model module'''

    def _import_(self):
        return __import__('noodle.core.model')

    def _session_(self):
        model = self._import_()
        engine = create_engine('sqlite:///:memory:')
        model.Session.configure(bind=engine)
        model.metadata.create_all(engine)  # @UndefinedVariable
        return model.Session()

    def test_import(self):
        '''Model can be imported'''
        import noodle.core.model  # @UnusedImport

    def test_create(self):
        '''Model metadata can be created'''
        from noodle.core.model import Session, metadata
        engine = create_engine('sqlite:///:memory:')
        Session.configure(bind=engine)
        metadata.create_all(engine)  # @UndefinedVariable

    def test_query(self):
        '''Model can be queried'''
        from noodle.core.model import Session, metadata, Share
        engine = create_engine('sqlite:///:memory:')
        Session.configure(bind=engine)
        metadata.create_all(engine)  # @UndefinedVariable
        Session().query(Share).all()
