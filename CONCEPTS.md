# Concepts

**Work in Progress**

## Filesystem abstraction layer

Noodle needs a filesystem abstraction layer to achieve independence
of the top-level components like the crawler or the proxy downloader
from the actual underlying filesystem which could be a normal local
filesystem or a network filesystem like FTP or CIFS.

Filesystem resources will be described by
[URLs](https://en.wikipedia.org/wiki/Uniform_resource_locator) which
are capable of denoting protocols, credentials, servers and the
filesystem structuring elements like directories and files.

The filesystem abstraction may be completely read-only.

To account for special needs (e.g. for network filesystems which need
to hold a connection to a remote host and the associated
credentials) all filesystem implementations need to be based on a 
root object which can do exactly that.

### Required features

**What features do all filesystem implementations have to provide?**
(Inspired by the ``os`` module)

* Listing directories (``os.listdir()``)
* Recursively walking directory structure (``os.walk()`` and ``os.path.walk()``)
* Reading file metadata (``os.stat()``, ``os.path.get*()``)
* Determining type of path (``os.path.isfile()``, ``os.path.isdir()``)
* Reading files (``open()``)

## Possible features

* Testing permissions on a path (``os.access()``, ``os.path.exists()``)
* Reading filesystem metadata (``os.statvfs()``)
* Symbolic link awareness (``os.lstat()``, ``os.readlink()``,
  ``os.path.lexists()``, ``os.path.islink()``)

### See also:

* [PEP 428 - object-oriented filesystem paths](http://www.python.org/dev/peps/pep-0428/)
  and the accompanying third-party library:
  [pathlib](https://pypi.python.org/pypi/pathlib/).
* Preliminary implementations and thoughts on the interface design:
  * [master@noodle-ng:crawler/filesystem.py](https://github.com/noodle-ng/noodle-ng/blob/master/crawler/filesystem.py) and
  * [develop@noodle-ng:crawling/__init__.py#L23](https://github.com/noodle-ng/noodle-ng/blob/develop/crawling/__init__.py#L23)
