#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various utility functions for XML.
"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###
	
def indent (elem, level=0, ind="  "):
	"""
	Mangle the text in an etree Element, so it prints with nice indents.
	
	Note that this actually mutates the etree, so it should be used with
	caution.
	
	Stolen from Elementree, so it can be used on etree.
	
	"""
	i = "\n" + level*ind
	if len (elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + ind
		for e in elem:
			indent(e, level+1, ind)
		if not e.tail or not e.tail.strip():
			e.tail = i
	if level and (not elem.tail or not elem.tail.strip()):
		elem.tail = i


	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
	_doctest()

	
### END ###################################################################
