#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various functions for manipulating dates and times.
"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import time
import datetime

__all__ = [

]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def str_to_datetime (strn, fmt):
	"""
	Convert a string to a datetime, as dictated by the given format.
	
	This is necessary as datetime only gets strptime in Python 2.5
	"""
	print "**%s**%s*", strn, fmt
	timetuple = time.strptime (strn, fmt)
	return datetime.datetime (*timetuple[:6])
	

### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
	_doctest()

	
### END ###################################################################
