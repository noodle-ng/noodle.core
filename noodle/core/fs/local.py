# -*- coding: utf-8 -*-
"""An example implementation of the filesystem abstraction layer
for a local filesystem"""

from noodle.core.fs import Filesystem

import os


class LocalFilesystem(Filesystem):
    """A Filesystem implementation for any kind of local filesystem"""

    _absolute_root = '/'

    def __init__(self, root='', absolute=True):
        """Initialize a LocalFilesystem object

        :param root: Root path in filesystem
        :param absolute:
            Whether to allow absolut paths in method calls.
            If this is :const:`True`, an absolute root path must be set.

        .. TODO::
            - Support for file:// URLs
            - Support absolute paths on windows
        """
        if not absolute and not self._is_absolute(root):
            # TODO: Automatically set root to cwd or raise?
            #root = os.getcwd()
            raise ValueError(root)
        self.root = root or ''
        self.absolute = absolute

    def _is_absolute(self, path):
        """Internal method to check whether path is absolute

        :param path: Path to check for being absolute
        :return: Whether path is absolute
        """
        return path.startswith(self._absolute_root)

    def abspath(self, path):
        """Return a normalized absolutized version of the pathname path.

        Mimicks the behaviour of :py:func:`os.path.abspath`

        :param path: Path to transform to absolute
        :return: Absolute version of path
        """
        if not self.absolute and self._is_absolute(path):
            raise ValueError(path)
        else:
            return os.path.normpath(os.path.join(self.root, path))

    def open(self, name):
        """open(name)

        Open a file, returns a file-like object.
        """
        return open(self.abspath(name))

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
