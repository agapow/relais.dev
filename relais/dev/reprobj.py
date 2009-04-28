#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A mixin class for simple rendering of an object as a string.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

__all__ = [
	'ReprObj',
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###	

class ReprObj (object):
	"""
	A class whose __str__ returns its __unicode__ as a UTF-8 bytestring.

	Useful as a mix-in.
	"""
	_repr_fields = [
		# override in base class
	]
	
	def __str__ (self):
		"""
		Return a nicely formatted string version of this object.
		
		This is simply the UTF-8 bytestring resulting from the __unicode__
		method.
		
		Stolen from django.utils.encoding.
		"""
		return self.__unicode__().encode ('utf-8')
		
	def __unicode__(self):
		"""
		Return a nicely formatted unicode version of this object.
		
		This gives the class name and all fields mentioned in the internal list
		of fields (`_repr_fields`). Note that all fields are sorted
		alphabetically and that if a field cannot be found, it is printed as
		'?'.
		"""
		repr_strs = ["%s: '%s'" % (field, getattr (self, field, '?')) for
			field in sorted (self._repr_fields)]
		return "%s (%s)" % (self.__class__.__name__, ', '.join (repr_strs))
		
	def __repr__ (self):
		"""
		Return a representation of this object.
		
		For this class, this is simply the string representation.
		"""
		return str (self)
	
	
	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
