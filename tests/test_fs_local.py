# -*- coding: utf-8 -*-

import unittest
import os, tempfile, shutil, stat as _stat

from noodle.core.fs.local import LocalFilesystem


class TestLocalFilesystem(unittest.TestCase):

    def setUp(self):
        self.rootdir = tempfile.mkdtemp()
        self.tempdir = tempfile.mkdtemp(dir=self.rootdir)
        self.tempdirname = os.path.basename(self.tempdir)
        _, self.tempfile = tempfile.mkstemp(dir=self.tempdir)
        self.tempfilename = os.path.basename(self.tempfile)

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_abspath(self):
        self.assertEqual(
            LocalFilesystem(self.rootdir).abspath(
                os.path.join(self.tempdirname, self.tempfilename)),
            self.tempfile)

    def test_open(self):
        LocalFilesystem().open(self.tempfile)

    def test_listdir_root(self):
        a = LocalFilesystem().listdir(self.rootdir)
        self.assertIn(self.tempdirname, a)
        b = LocalFilesystem(self.rootdir).listdir()
        self.assertIn(self.tempdirname, b)
        self.assertItemsEqual(a, b)

    def test_listdir_sub(self):
        a = LocalFilesystem().listdir(os.path.join(self.rootdir, self.tempdirname))
        self.assertIn(self.tempfilename, a)
        b = LocalFilesystem(self.rootdir).listdir(self.tempdirname)
        self.assertIn(self.tempfilename, b)
        self.assertItemsEqual(a, b)

    def test_listdir_no_absolute(self):
        lfs = LocalFilesystem(self.rootdir, absolute=False)
        l = lfs.listdir(self.tempdirname)
        self.assertIn(self.tempfilename, l)
        with self.assertRaises(ValueError):
            lfs.listdir(self.tempdir)

    def test_listdir_no_absolute_no_root(self):
        with self.assertRaises(ValueError):
            LocalFilesystem(absolute=False)

    def test_walk(self):
        walk = list(LocalFilesystem(self.rootdir).walk(''))
        self.assertEqual(
            [(self.rootdir, [self.tempdirname], []),
                (self.tempdir, [], [self.tempfilename])],
            walk)

    def test_path_walk(self):
        walk = list()
        def func(arg, top, names):
            walk.extend(names)
        LocalFilesystem().path_walk(self.rootdir, func=func, arg=None)
        self.assertSequenceEqual([self.tempdirname, self.tempfilename], walk)

    def test_stat_and_get_star(self):
        lsf = LocalFilesystem()
        stat = lsf.stat(self.tempfile)
        atime = lsf.getatime(self.tempfile)
        self.assertAlmostEqual(atime, stat[_stat.ST_ATIME], delta=1.0)
        ctime = lsf.getctime(self.tempfile)
        self.assertAlmostEqual(ctime, stat[_stat.ST_CTIME], delta=1.0)
        mtime = lsf.getmtime(self.tempfile)
        self.assertAlmostEqual(mtime, stat[_stat.ST_MTIME], delta=1.0)
        size = lsf.getsize(self.tempfile)
        self.assertEqual(size, stat[_stat.ST_SIZE])

    def test_isdir(self):
        self.assertTrue(LocalFilesystem().isdir(self.tempdir))

    def test_isfile(self):
        self.assertTrue(LocalFilesystem().isfile(self.tempfile))
