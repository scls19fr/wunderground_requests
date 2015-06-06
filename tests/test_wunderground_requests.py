#!/usr/bin/env python
# encoding: utf-8

from nose.tools import raises, with_setup, eq_, ok_

import wunderground_requests
from wunderground_requests import *
import datetime
#import logging
import six

def test_version():
    """Test version"""
    version = wunderground_requests.__version__
    print(version)
    assert(isinstance(version, six.string_types))

