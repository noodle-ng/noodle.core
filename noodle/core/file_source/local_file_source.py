from abstract_file_source import AbstractFileSource
import os


class LocalFileSource(AbstractFileSource):

    def __init__(self, root):
        """init file source with root node destination"""

        self.root = root

    def list_content(self, basedir=None):
        """list content in basedir"""

        if basedir is None:
            basedir = self.root

        os.chdir(basedir)
        entries = os.listdir(basedir)

        files = filter(os.path.isfile, entries)
        folders = filter(os.path.isdir, entries)

        return basedir, folders, files

    def walk_content(self, basedir=None):
        """walk content from basedir"""

        if basedir is None:
            basedir = self.root

        return list(os.walk(basedir))

    def get_meta_data(self, target, verbose=False):
        """get meta data dictionary from given target"""

        raise NotImplementedError()

    def get_file_handler(self, offset=0):
        """get a file handler with offset"""

        raise NotImplementedError()

if __name__ == '__main__':

    share = LocalFileSource("/home")
    print share.list_content("/tmp")
    print share.walk_content("/tmp")
