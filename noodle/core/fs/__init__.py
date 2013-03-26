# -*- coding: utf-8 -*-
"""The filesystem abstraction layer

The class Filesystem is an abstract base class/interface for a valid
filesystem abstraction implementation.
"""


class Filesystem(object):
    """Abstract base class for the filesystem abstraction layer"""

    def __init__(self):
        """Initialize a Filesystem object

        For a local filesystem, this could contain a root directory
        to which all further operations are relative to.
        For a remote filesystem, this could hold the host and
        credential data and the remote connection object.
        """
        raise NotImplementedError()

    def listdir(self, path):
        """os.listdir(path)

        Return a list containing the names of the entries in the directory.
        """
        raise NotImplementedError()

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
