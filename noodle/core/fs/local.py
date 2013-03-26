# -*- coding: utf-8 -*-
"""An example implementation of the filesystem abstraction layer
for a local filesystem"""

from noodle.core.fs import Filesystem

import os


pathjoin = os.path.join


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

    def listdir(self, path=''):
        """os.listdir(path)

        Return a list containing the names of the entries in the directory.

        If path is not set, it will be attempted to list the contents
        of the root directory.
        """
        if not self.absolute and self._is_absolute_(path):
            raise ValueError(path)
        return os.listdir(pathjoin(self.root, path))

    def walk(self, top, topdown=True, onerror=None, followlinks=False):
        """os.walk(top, topdown=True, onerror=None, followlinks=False)

        Directory tree generator.
        """
        raise NotImplementedError()

    def path_walk(self, top, func, arg):
        """os.path.walk(top, func, arg)

        Directory tree walk with callback function.
        """
        raise NotImplementedError()

    def stat(self, path):
        """os.stat(path)

        Perform a stat call on the given path, returns a stat result tuple.
        """
        raise NotImplementedError()

    def getatime(self, filename):
        """os.path.getatime(filename)

        Return the last access time of a file, reported by os.stat().
        """
        raise NotImplementedError()

    def getctime(self, filename):
        """os.path.getctime(filename)

        Return the metadata change time of a file, reported by os.stat().
        """
        raise NotImplementedError()

    def getmtime(self, filename):
        """os.path.getmtime(filename)

        Return the last modification time of a file, reported by os.stat().
        """
        raise NotImplementedError()

    def getsize(self, filename):
        """os.path.getsize(filename)

        Return the size of a file, reported by os.stat().
        """
        raise NotImplementedError()

    def isdir(self, s):
        """os.path.isdir(s)

        Return true if the pathname refers to an existing directory.
        """
        raise NotImplementedError()

    def isfile(self, s):
        """os.path.isfile(s)

        Test whether a path is a regular file
        """
        raise NotImplementedError()

    def open(self, name):
        """open(name)

        Open a file, returns a file-like object.
        """
        raise NotImplementedError()


if __name__ == '__main__':
    print LocalFilesystem().listdir('/')
    print LocalFilesystem('/usr').listdir('/')
    print LocalFilesystem('/usr', absolute=False).listdir('share')
