#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Common exception types.

"""
# NOTE: 20071125 tested and passed.

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import exceptions

## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###

class FormatError (exceptions.Exception):
	# TODO: needs file and line arguments as well?
	def __init__ (self, value):
		self.value = value

	def __str__(self):
		return repr (self.value)




### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
