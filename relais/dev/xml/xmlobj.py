#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A mixin class for simple rendering of an object as XML.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

#__all__ = [
#	'TagAttrib',
#]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###	

class XmlObj (object):
	"""
	A class whose __str__ returns its __unicode__ as a UTF-8 bytestring.

	Useful as a mix-in.
	"""
	
	# override in base class
	_xml_tag = ''
	_xml_attribs = []
	_xml_fields = []
	
	def as_xml (self):
		""".
		"""
		pass
		

	
	
	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
