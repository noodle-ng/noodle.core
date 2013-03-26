# -*- coding: utf-8 -*-

import unittest, nose.tools as nosetools
import os, tempfile, shutil, stat as _stat

from noodle.core.fs import Filesystem


class TestFilesystem(unittest.TestCase):

    def test_init(self):
        '''Filesystem initialization'''
        Filesystem()

    @nosetools.raises(NotImplementedError)
    def test_abspath(self):
        '''Filesystem abspath'''
        Filesystem().abspath('')

    @nosetools.raises(NotImplementedError)
    def test_open(self):
        '''Filesystem open'''
        Filesystem().open('')

    @nosetools.raises(NotImplementedError)
    def test_listdir(self):
        '''Filesystem listdir'''
        Filesystem().listdir('')

    @nosetools.raises(NotImplementedError)
    def test_walk(self):
        '''Filesystem walk'''
        Filesystem().walk('')

    @nosetools.raises(NotImplementedError)
    def test_path_walk(self):
        '''Filesystem path_walk'''
        Filesystem().path_walk('', func=lambda arg, top, names: names, arg=None)

    @nosetools.raises(NotImplementedError)
    def test_stat(self):
        '''Filesystem stat'''
        Filesystem().stat('')

    @nosetools.raises(NotImplementedError)
    def test_atime(self):
        '''Filesystem atime'''
        Filesystem().getatime('')

    @nosetools.raises(NotImplementedError)
    def test_ctime(self):
        '''Filesystem ctime'''
        Filesystem().getctime('')

    @nosetools.raises(NotImplementedError)
    def test_mtime(self):
        '''Filesystem mtime'''
        Filesystem().getmtime('')

    @nosetools.raises(NotImplementedError)
    def test_size(self):
        '''Filesystem size'''
        Filesystem().getsize('')

    @nosetools.raises(NotImplementedError)
    def test_isdir(self):
        '''Filesystem isdir'''
        Filesystem().isdir('')

    @nosetools.raises(NotImplementedError)
    def test_isfile(self):
        '''Filesystem isfile'''
        Filesystem().isfile('')
