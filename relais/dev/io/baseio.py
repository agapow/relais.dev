#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A base class for all readers and writers.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import os

from relais.dev import fileutils


__all__ = [
	'BaseIO',
]


## CONSTANTS & DEFINES ###

class BaseIO (object):
	"""
	A base class for all readers and writers.

	"""
	def __init__ (self, hndl, mode='rb', fmt=None):
		"""
		Class c'tor.

		:Params:
			hndl
				The output (or input) for the object, being a file path or an open
				and writable (or readable) file-like object.
			mode
				What mode to open any file path as, if necessary. If an open
				file-like is supplied, obviously this won't be used. By default,
				it is set to 'rb', the least destructive option. Derived classes
				should obviously override this.
			fmt
				The file format. This is case-insensitive and if not given is
				derived from the handles ``name`` attribute. Obviously, it's
				an error if the handle has no name.
		
		Note that if an open handle is passed to the reader it will not close
		it, but if it has to open a handle, it will close it.
		
		"""
		## Preconditions & preparations:
		# if file is a filename
		if (isinstance (hndl, basestring)):
			hndl = open (hndl, mode)
			hndl_opened = True
		else:
			hndl_opened = False
		self.hndl = hndl
		self.hndl_opened = hndl_opened
		# determine & normalise format if need be
		self.fmt = self.get_format (fmt)
		## Main:
		
	def __del__ (self):
		"""
		Note this may generate an error if the object is disposed of unnaturally.
		"""
		try:
			if (self.hndl_opened):
				self.hndl.close()
		except:
			pass
	
	## INTERNALS:		
	def get_format (self, fmt, lower=True):
		"""
		Return the extension of a filename.

		:Params:
			fname
				A file name or path.
			lower
				Should the derived extension be given as lowercase?

		"""
		if (fmt is not None):
			if (lower):
				fmt = fmt.lower()
			return fmt
		else:
			# TODO: place with utilities?
			fname = getattr (self.hndl, 'name')
			if (fname is None):
				return None
			return fileutils.ext_from_filepath (fname, lower)



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
