#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An base class for all writers.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from exceptions import NotImplementedError

import basewriter

__all__ = [
	'BaseWriter',
]


## CONSTANTS & DEFINES ###

class RecordWriter (basewriter.BaseWriter):
	"""
	A base class for all all writers.

	"""
	def __init__ (self, dst, mode='w', fmt=None):
		"""
		Class c'tor.

		:Params:
			dst
				The output point for the writer, a file path or an open and
				writable file-like object.
			mode
				What mode to open any output file path as.
			fmt
				The file format.
		
		Note that if an open handle is passed to the reader it will not close
		it, but if it has to open a handle, it will close it.
		
		"""
		basewriter.BaseWriter.__init__ (self, dst, mode=mode, fmt=fmt)
		
		
	def __del__ (self):
		"""
		Class d'tor.
		
		This exists purely to flush the writer before destroying it.
		"""
		self.flush()
		
	## MUTATORS:
	def write (self, rec):
		"""
		Write a single record to the output.

		"""
		raise NotImplementedError ('must override method in subclass')

	def write_iter (self, recs):
		"""
		For every record in an iterable, write it.
		"""
		for r in recs:
			self.write (rec)
	
	def flush (self):
		"""
		Write any accumulated output to the destination.
		"""
		raise NotImplementedError ('must override method in subclass')
	
	## INTERNALS:



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
