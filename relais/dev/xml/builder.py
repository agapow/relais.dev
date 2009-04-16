#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Class for constructing and writing XML trees.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import etreewriter
from etree import (Element, ElementTree)


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class BaseBuilder (object):
	"""
	A base class for building etree ElementTrees.
	
	This class forms a base for builders that provide a friendly interface
	to constructing etrees. Derived classes should provide an interface that
	at least makes it dificult to build any illegal trees.
	
	By convention, 'new' methods create and return a new element or tree of
	elements, unattached to the growing document. 'add' methods do the same,
	but add the new constructs to a designated point in the tree.
	
	"""
	def __init__ (self, root_tag, **kwargs):
		"""
		C'tor, creating the XML document and root element.
		
		:Parameters:
			root_tag
				The type / name of the root element of the document.
			encoding
				The encoding to be used (and stated) in the final output.
			kwargs
				Attributes on the root element.
				
		"""
		self._tree = ElementTree
		self.root = Element (root_tag, **kwargs)
		
	def new_element (self, tag, **kwargs):
		"""
		Create an new element.
		
		:Parameters:
			tag
				The type / name of the new element document.
			kwargs
				Attributes on the new element.
			
		:Returns:
			The new element.
			
		This is just a convenience method, that also wraps any difference
		between the various etree libraries.
			
		"""
		return Element (tag, **kwargs)
		
	def add_element (self, parent, tag, **kwargs):
		"""
		Create a new element and add it to the growing document.

		:Parameters:
			parent
				The element this new element will be appended to.
			tag
				The type / name of the new element document.
			kwargs
				Attributes on the new element.

		:Returns:
			The new element.

		"""
		return SubElement (parent, tag, **kwargs)

		
	def write (self, dst, encoding='utf8', prettyprint=False):
		etreewriter.write_etree (self.root, dst, encoding, prettyprint)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
	_doctest()

	
### END ###################################################################
