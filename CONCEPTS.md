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

### Required features

**What features do all filesystem implementations have to provide?**
(Inspired by the ``os`` module)

* Listing directories (``os.listdir()``)
* Recursively walking directory structure (``os.walk()`` and ``os.path.walk()``)
* Reading file metadata (``os.stat()``)
* Reading files (``open()``)

### See also:

* [PEP 428 - object-oriented filesystem paths](http://www.python.org/dev/peps/pep-0428/)
  and the accompanying third-party library:
  [pathlib](https://pypi.python.org/pypi/pathlib/).
* Preliminary implementations and thoughts on the interface design:
  [master@noodle-ng:crawler/filesystem.py](https://github.com/noodle-ng/noodle-ng/blob/master/crawler/filesystem.py) and
  [develop@noodle-ng:crawling/__init__.py#L23](https://github.com/noodle-ng/noodle-ng/blob/develop/crawling/__init__.py#L23)
