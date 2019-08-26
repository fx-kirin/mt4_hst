#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import logging
import os

import kanilog
import pytest
import stdlogging
from add_parent_path import add_parent_path

with add_parent_path():
    import mt4_hst


def setup_module(module):
    pass


def teardown_module(module):
    pass


def setup_function(function):
    pass


def teardown_function(function):
    pass


def test_func():
    pass


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    kanilog.setup_logger(logfile='/tmp/%s.log' % (os.path.basename(__file__)), level=logging.INFO)
    stdlogging.enable()

    pytest.main([__file__, '-k test_', '-s'])
