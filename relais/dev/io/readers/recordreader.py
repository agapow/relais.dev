#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for all readers that can read a record at a time.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from exceptions import NotImplementedError

import basereader

__all__ = [
	'RecordReader',
]


## CONSTANTS & DEFINES ###

class RecordReader (basereader.BaseReader):
	"""
	A base class for all readers.

	"""
	def __init__ (self, src, mode='r', fmt=None):
		"""
		Class c'tor.

		:Params:
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
		basereader.BaseReader.__init__ (self, src, mode=mode, fmt=fmt)
		
	## MUTATORS:
	def read (self):
		"""
		Read a single record from the input.

		"""
		raise NotImplementedError ('must override method in subclass')

	def __iter__ (self, recs):
		"""
		Iterate over every record in the source.
		"""
		while (not self.at_end()):
			yield self.read()
	
	## INTERNALS:
	def at_end (self):
		raise NotImplementedError ('must override method in subclass')



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
