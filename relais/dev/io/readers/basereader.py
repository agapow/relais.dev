#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for all readers.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from exceptions import NotImplementedError

from relais.dev.io.baseio import BaseIO

__all__ = [
	'BaseReader',
]


## CONSTANTS & DEFINES ###

class BaseReader (BaseIO):
	"""
	A base class for all readers.

	"""
	def __init__ (self, src, mode='r', fmt=None):
		"""
		Class c'tor.

		:Parameters:
			src
				The input point for the writer, a file path or an open and
				readable file-like object.
			mode
				What mode to open any output file path as.
			fmt
				The file format.
		
		Note that if an open handle is passed to the reader it will not close
		it, but if it has to open a handle, it will close it.
		
		"""
		BaseIO.__init__ (self, src, mode=mode, fmt=fmt)
		



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
