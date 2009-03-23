#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various functions for using the xml.etree / ElementTree packages..
"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

try:
	from xml.etree.ElementTree import (
		Element,
		SubElement,
		ElementTree,
		iselement,
		parse,
	)
	
except:
	from elementtree.ElementTree import (
		Element,
		SubElement,
		ElementTree,
		iselement,
		parse,
	)


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def new_element (tag, attrib={}, children=[], **kwargs):
	elem = Element (tag, attrib, **kwargs)
	return elem



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
	_doctest()

	
### END ###################################################################
