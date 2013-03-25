Concepts
========

**Conceptual design decisions are still Work in Progress**

Filesystem abstraction layer
----------------------------

Noodle needs a filesystem abstraction layer to achieve independence
of the top-level components like the crawler or the proxy downloader
from the actual underlying filesystem which could be a normal local
filesystem or a network filesystem like FTP or CIFS.

Filesystem resources will be described by URLs which are capable of
denoting protocols, credentials, servers and the default filesystem
structuring elements like directories and files.

What features do all filesystem implementations have to provide?

* Listing directories (recursive, too)
* Reading file metadata
* Reading files

