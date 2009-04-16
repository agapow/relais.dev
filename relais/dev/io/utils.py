#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Some utilities for IO.

"""
# NOTE: 20071125 tested and passed.

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import cStringIO

from relais.dev.rcheck import assert_file_exists

__all__ = [
	'readaable_from_string',
	'make_readable_handle',
	'make_writable_handle',
]


## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###

def readaable_from_string (strn):
	"""
	Make a readable buffer from a string.
	
	
	"""
	return cStringIO.StringIO (strn)


def make_writable_handle (dest, mode='w'):
	"""
	If not a writable file-like object, open as a file path for writing.
	"""
	if (not hasattr (dest, 'write')):
		assert_file_exists (dest)
		dest = open (dest, mode)
	return dest



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
