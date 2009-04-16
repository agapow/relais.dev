#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple class for holding options.

"""

__docformat__ = 'restructuredtext en'



### IMPORTS ###

__all__ = [
	'IoOptions',
]


### CONSTANTS & DEFINES ###

ALLOWED = True
FORBIDDEN = False


### IMPLEMENTATION ###

class Options (dict):
	"""
	A class for collecting options, particularily for readers/writers.

	IO classes tend to accumulate a lot of options, that over time leads to
	lengthy and and confused calling signatures::
	
		MyReader (prettyprint=False, encoding='utf8', quote_names=True,
			escape_entities=False, ...)
	
	This class is a way of gathering all those options into a single argument,
	aiding readability while allowing default and user values aw well as
	validation. It behaves (and is derived from) a simple dictionary, with the
	exception of the initial default values and validation.
	
	"""
	# TODO: repurpose as general options class?
	
	# default values for options, override in derived class
	defaults = {}
	allowed_fields = []
	
	def __init__ (self, *args, **kwargs):
		"""
		C'tor, allowing initial values.
		
		The dialect object can be initialised just like a dictionary. If a
		mapping is defined in the class `defaults` member, this is set before
		any passed in options. That is, user options override defaults.
		"""
		# awkward juggling of dicts, but only way to get right behaviour
		default_options = self.defaults.copy()
		new_options = dict (*args, **kwargs)
		default_options.update (new_options)
		dict.__init__ (self, default_options)
		self._validate()
		
	def _validate (self):
		pass




### TEST & DEBUG ###

def _doctest ():
   import doctest
   doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
   _doctest()


### END ########################################################################
