# -*- coding: utf-8 -*-
"""Development test script for the plugins"""

import pkg_resources


if __name__ == '__main__':
    for entrypoint in pkg_resources.iter_entry_points('noodle.plugins'):
        print entrypoint
        # Grab the function that is the actual plugin.
        plugin = entrypoint.load()  # Call the plugin
        print plugin
        print dir(plugin)
        try:
            print plugin.hello
        except:
            pass
