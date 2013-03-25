# -*- coding: utf-8 -*-
""""""

class AbstractFileSource(object):
    """"""

    def __init__(self, root):
        """init file source with root node destination"""
        raise NotImplementedError()


    def list_content(self, basedir=None):
        """list content in basedir"""
        
        raise NotImplementedError()

    def walk_content(self, basedir=None):
        """walk content from basedir"""
        
        raise NotImplementedError()
    
    def get_meta_data(self, target, verbose=False):
        """get meta data dictionary from given target"""
        raise NotImplementedError()

    def get_file_handler(self, offset=0):
        """get a file handler with offset"""
        raise NotImplementedError()

if __name__ == '__main__':
    
    share = AbstractFileSource("/home")
    print share.list_content("/tmp")
    print share.walk_content("/tmp")

