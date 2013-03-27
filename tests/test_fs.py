# -*- coding: utf-8 -*-

import unittest, nose.tools as nosetools
import os, tempfile, shutil, stat as _stat

from noodle.core.fs import Filesystem


class MockFilesytem(Filesystem):
    '''Mocked Filesystem implementation to allow object initialization'''

    def __init__(self):
        pass


class TestFilesystem(unittest.TestCase):

    @nosetools.raises(NotImplementedError)
    def test_init(self):
        '''Filesystem initialization'''
        Filesystem()

    @nosetools.raises(NotImplementedError)
    def test_abspath(self):
        '''Filesystem abspath'''
        MockFilesytem().abspath('')

    @nosetools.raises(NotImplementedError)
    def test_open(self):
        '''Filesystem open'''
        MockFilesytem().open('')

    @nosetools.raises(NotImplementedError)
    def test_listdir(self):
        '''Filesystem listdir'''
        MockFilesytem().listdir('')

    @nosetools.raises(NotImplementedError)
    def test_walk(self):
        '''Filesystem walk'''
        MockFilesytem().walk('')

    @nosetools.raises(NotImplementedError)
    def test_path_walk(self):
        '''Filesystem path_walk'''
        MockFilesytem().path_walk('', func=lambda arg, top, names: names, arg=None)

    @nosetools.raises(NotImplementedError)
    def test_stat(self):
        '''Filesystem stat'''
        MockFilesytem().stat('')

    @nosetools.raises(NotImplementedError)
    def test_atime(self):
        '''Filesystem atime'''
        MockFilesytem().getatime('')

    @nosetools.raises(NotImplementedError)
    def test_ctime(self):
        '''Filesystem ctime'''
        MockFilesytem().getctime('')

    @nosetools.raises(NotImplementedError)
    def test_mtime(self):
        '''Filesystem mtime'''
        MockFilesytem().getmtime('')

    @nosetools.raises(NotImplementedError)
    def test_size(self):
        '''Filesystem size'''
        MockFilesytem().getsize('')

    @nosetools.raises(NotImplementedError)
    def test_isdir(self):
        '''Filesystem isdir'''
        MockFilesytem().isdir('')

    @nosetools.raises(NotImplementedError)
    def test_isfile(self):
        '''Filesystem isfile'''
        MockFilesytem().isfile('')
