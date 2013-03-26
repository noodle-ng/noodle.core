# -*- coding: utf-8 -*-

import unittest

from noodle.core.fs.local import LocalFilesystem


class TestLocalFilesystem(unittest.TestCase):

    def test_listdir_root(self):
        a = LocalFilesystem().listdir('/')
        self.assertIn('usr', a)
        b = LocalFilesystem('/').listdir()
        self.assertIn('usr', b)
        self.assertItemsEqual(a, b)

    def test_listdir_sub(self):
        a = LocalFilesystem().listdir('/usr')
        self.assertIn('share', a)
        b = LocalFilesystem('/').listdir('usr')
        self.assertIn('share', b)
        self.assertItemsEqual(a, b)

    def test_listdir_no_absolute(self):
        lfs = LocalFilesystem('/', absolute=False)
        l = lfs.listdir('usr')
        self.assertIn('share', l)
        with self.assertRaises(ValueError):
            lfs.listdir('/usr')

    def test_listdir_no_absolute_no_root(self):
        with self.assertRaises(ValueError):
            LocalFilesystem(absolute=False)
