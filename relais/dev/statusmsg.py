#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple representation of status messages.

It's often necessary to pass or store messages for informing users.
Additionally, some messages will be critical while others will be simply
informative, e.g. reporting errors or possible inconsistencies from parsing.
This module provides a simple structure for these messages, with little
functionality but aiding readability and consistency.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import enum, reprobj

__all__ = [
	'StatusMsg',
]


### CONSTANTS & DEFINES ###

MSG_CLASS = enum.Enum (
	'info',
	'warning',
	'error',
)


### IMPLEMENTATION ###

class StatusMsg (reprobj.ReprObj):
	"""
	A simple representation of a status message.
	
	"""
	_repr_fields = [
		'type',
		'msg',
	]
		
	def __init__ (self, type, msg):
		"""
		C'tor.
		
		Subclasses may need to initialise their renaming machinery in their own
		c'tor.
		"""
		self.type = type
		self.msg = msg
		
	def __cmp__ (self, rhs):
		"""
		Sort status messages by type and then message content.
		"""
		if (isinstance (rhs, self.__class__)):
			return cmp (self.type, rhs.type) or cmp (self.msg, rhs.msg)
		else:
			return reprobj.ReprObj.__cmp__ (self, rhs)
	

def info (msg):
	"""
	Convenience function for generating an "info" class status message.
	"""
	return StatusMsg (MSG_CLASS.info, msg)
	
	
def warning (msg):
	"""
	Convenience function for generating an "warning" class status message.
	"""
	return StatusMsg (MSG_CLASS.warning, msg)
	
	
def error (msg):
	"""
	Convenience function for generating an "error" class status message.
	"""
	return StatusMsg (MSG_CLASS.error, msg)
	
	
	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
