#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simpled enumerated constants for Python.


For example::

	Days = Enum('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')
	print Days
	print Days.Mo
	print Days.Fr
	print Days.Mo < Days.Fr
	print list(Days)
	for each in Days:
		print 'Day:', each

	Confirmation = Enum ('No', 'Yes')
	answer = Confirmation.No
	print 'Your answer is not', ~answer
	
Lifted from Zoran Isailovski's recipe.

"""
# TODO: could be easily extended to metaclasses and to accept dict or set
# as arg. See <http://code.activestate.com/recipes/81098/>

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import cStringIO, os


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def Enum (*names):

	class EnumClass (object):
		__slots__ = names
		def __iter__ (self):
			return iter (constants)
			
		def __len__ (self):
			return len (constants)
			
		def __getitem__ (self, i):
			return constants[i]
			
		def __repr__ (self):
			return 'Enum' + str (names)
			
		def __str__ (self):
			return 'enum ' + str (constants)

	class EnumValue (object):
		__slots__ = ('__value')
		
		def __init__(self, value):
			self.__value = value
			
		Value = property (lambda self: self.__value)
		EnumType = property (lambda self: EnumType)
		
		def __hash__(self):
			return hash(self.__value)
			
		def __cmp__(self, other):
			# C fans might want to remove the following assertion
			# to make all enums comparable by ordinal value {;))
			assert self.EnumType is other.EnumType, "Only values from the same enum are comparable"
			return cmp (self.__value, other.__value)
			
		def __invert__(self):
			return constants[maximum - self.__value]
			
		def __nonzero__(self):
			return bool(self.__value)
			
		def __repr__(self):
			return str(names[self.__value])

	maximum = len (names) - 1
	constants = [None] * len (names)
	for i, each in enumerate (names):
		val = EnumValue (i)
		setattr (EnumClass, each, val)
		constants[i] = val
	constants = tuple (constants)
	EnumType = EnumClass()
	return EnumType





### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
	_doctest()

	
### END ###################################################################
