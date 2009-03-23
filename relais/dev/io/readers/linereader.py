#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
A line-oriented reader.

"""

### IMPORTS ###

import recordreader

__all__ = [
	'LineReader',
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class LineReader (recordreader.RecordReader):
	"""
	A line-oriented reader.
	"""
	def __init__ (self, src):
		"""
		Class c'tor.
		
		"""
		basereader.BaseReader.__init__ (self, src, fmt='txt')
		self.buf = self._readline()
		
	## MUTATORS:
	def read (self):
		"""
		Read a single line from the input.

		"""
		tmp = self.buf
		self.buf = self._readline()
		return tmp
	
	## INTERNALS:
	def at_end (self):
		return (not self.buf)
		
	def _readline (self):
		return self.hndl.readline()



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
