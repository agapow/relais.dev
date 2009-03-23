#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Some utilities for development.

"""
# NOTE: 20071125 tested and passed.

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import warnings
import exceptions
import types
import os

from relais.dev import debug


## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###


### DICT UTILS

def get_dictval (d, keys, default=None):
	"""
	Check a dictionary for various keys and return the first associated value.
	
	This is necessitated by the changing field names.
	"""
	for item in keys:
		if d.has_key (item):
			return d[item]
	return default



### EXCEPTIONS

class FormatError (exceptions.Exception):
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
