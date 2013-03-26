noodle.core
===========

**Noodle NG Core Components**

This project contains only the core components for the Noodle NG file search engine:
The database model and some auxiliary functions.
It should depend on as little other packages as possible!

[![Build Status](https://travis-ci.org/noodle-ng/noodle.core.png)](https://travis-ci.org/noodle-ng/noodle.core)

Installation/Usage
------------------

As this project is currently in development and has not been released yet, the
recommended way to install and use it is by checking out the Git repository and
installing it in develop mode within a clean Python [virtualenv]
(http://www.virtualenv.org).

The usage of [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org)
is recommended, as it makes handling of many different virtualenvs a lot
easier:

    $ mkvirtualenv noodle

Without virtualenvwrapper:

    $ virtualenv noodle
    $ cd noodle
    $ source bin/activate

Then, check out this repository and install the package in development mode:

    $ git clone https://github.com/noodle-ng/noodle.core.git
    $ cd noodle.core
    $ python setup.py develop
