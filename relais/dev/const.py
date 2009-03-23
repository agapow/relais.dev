#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Constants for Python.

Attributes created within this module can be created and bound once, but not
reassigned. For example::

	import const
	const.magic = 23
	const.magic = 88

Lifted from Alex Martelli's recipe.

"""
# NOTE: 20071125 tested and passed.

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from exceptions import TypeError, KeyError


## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###

class _const:
	__name__ = 'relais.dev.const'
	
	class ConstError (TypeError):
		pass
		
	def __setattr__ (self, name, value):
		if self.__dict__.has_key (name):
			raise self.ConstError, "Can't rebind const (%s)" % name
		self.__dict__[name] = value
		
	def __delattr__ (self, name):
		if self.__dict__.has_key (name):
			raise self.ConstError, "Can't delete const (%s)" % name
		else:
			raise KeyError, "Const (%s) does not exist" % name
		
import sys
sys.modules[__name__] = _const()




### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
