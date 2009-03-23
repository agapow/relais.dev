#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various functions for manipulating files and handles.
"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import cStringIO, os


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def string_to_handle (in_str):
	"""
	Converts a string to a suitable open handle for parsers.
	
	Note: this is like a file that has already been opened.
	"""
	return cStringIO.StringIO (in_str)


def ext_from_filepath (fpath, lower=True):
	"""
	Return the extension of this file name or path.
	
	:Params:
		fpath
			File name or path
		lower
			Normalise the extension to lower case.
			
	:Returns:
		The file extension, without the seperator / do character.
		
	"""
	basename, ext = os.path.splitext (fpath)
	if ext.startswith (os.extsep):
		ext = ext[len (os.extsep):]
	if (lower):
		ext = ext.lower()
	return ext


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
	_doctest()

	
### END ###################################################################
