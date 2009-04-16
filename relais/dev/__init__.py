#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Assorted development facilities for Relais.

There are various debugging and development functions used throughout Relais,
as well as a number of interfaces for common tasks (e.g. IO, mountpoints).
Rather than attach these to another module (fattening and confusing its API in
the process), these have been broken out into their own module.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

## CONSTANTS & DEFINES ###

__version__ = "0.2"


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
