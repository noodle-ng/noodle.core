# -*- coding: utf-8 -*-
"""An example implementation of the filesystem abstraction layer
for a local filesystem"""

from noodle.core.fs import Filesystem

import os


class LocalFilesystem(Filesystem):
    """"""

    absolute_root = '/'

    def __init__(self, root='', absolute=True):
        """Initialize a Filesystem object

        If root is set, all further operations will be relative
        to it.
        If absolute is True, all other methods will accept
        absolute paths (i.e. paths starting with '/')
        If absolute is False, absolute paths will be rejected.

        TODO: Support for file:// URLs
        TODO: Support absolute paths on windows
        """
        if not absolute and not self._is_absolute_(root):
            # TODO: Automatically set root to cwd or raise?
            #root = os.getcwd()
            raise ValueError(root)
        self.root = root or ''
        self.absolute = absolute

    def _is_absolute_(self, path):
        """Internal method to check whether path is absolute"""
        return path.startswith(self.absolute_root)

    def abspath(self, path):
        """os.path.abspath(path)

        Return a normalized absolutized version of the pathname path.
        """
        if not self.absolute and self._is_absolute_(path):
            raise ValueError(path)
        else:
            return os.path.normpath(os.path.join(self.root, path))

    def listdir(self, path=''):
        """os.listdir(path)

        Return a list containing the names of the entries in the directory.

        If path is not set, it will be attempted to list the contents
        of the root directory.
        """
        return os.listdir(self.abspath(path))

    def walk(self, top, topdown=True, onerror=None, followlinks=False):
        """os.walk(top, topdown=True, onerror=None, followlinks=False)

        Directory tree generator.
        """
        return os.walk(self.abspath(top), topdown, onerror, followlinks)

    def path_walk(self, top, func, arg):
        """os.path.walk(top, func, arg)

        Directory tree walk with callback function.
        """
        return os.path.walk(self.abspath(top), func, arg)

    def stat(self, path):
        """os.stat(path)

        Perform a stat call on the given path, returns a stat result tuple.
        """
        return os.stat(self.abspath(path))

    def getatime(self, filename):
        """os.path.getatime(filename)

        Return the last access time of a file, reported by os.stat().
        """
        return os.path.getatime(self.abspath(filename))

    def getctime(self, filename):
        """os.path.getctime(filename)

        Return the metadata change time of a file, reported by os.stat().
        """
        return os.path.getctime(self.abspath(filename))

    def getmtime(self, filename):
        """os.path.getmtime(filename)

        Return the last modification time of a file, reported by os.stat().
        """
        return os.path.getmtime(self.abspath(filename))

    def getsize(self, filename):
        """os.path.getsize(filename)

        Return the size of a file, reported by os.stat().
        """
        return os.path.getsize(self.abspath(filename))

    def isdir(self, s):
        """os.path.isdir(s)

        Return true if the pathname refers to an existing directory.
        """
        return os.path.isdir(self.abspath(s))

    def isfile(self, s):
        """os.path.isfile(s)

        Test whether a path is a regular file
        """
        return os.path.isfile(self.abspath(s))

    def open(self, name):
        """open(name)

        Open a file, returns a file-like object.
        """
        return open(self.abspath(name))
