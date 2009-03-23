#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Common development calls.

For ease of use, the most common utlities in relais.dev are available from
this package and can be accessed with a simple::

	from relais.dev.common import *

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from relais.dev.debug import *
from relais.dev.rcheck import *


## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###

### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
