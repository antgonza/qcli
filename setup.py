#!/usr/bin/env python

__author__ = "The BiPy Development Team"
__copyright__ = "Copyright 2013, The BiPy Project"
__credits__ = ["Rob Knight", "Greg Caporaso", ] 
__license__ = "GPL"
__version__ = "0.0.0-dev"
__maintainer__ = "Greg Caporaso"
__email__ = "gregcaporaso@gmail.com"
__status__ = "Development"

from distutils.core import setup
from glob import glob

setup(name='qcli',
      version='0.0.0-dev',
      packages=['qcli'],
      scripts=glob('scripts/qcli*')
      )