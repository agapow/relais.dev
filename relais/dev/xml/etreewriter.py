#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An XML writer that accepts etree / ELementTree data.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from copy import deepcopy

from relais.dev.xml.etree import (
	Element,
	ElementTree,
	iselement,
)
from utils import indent

from relais.dev.io.writers.basewriter import BaseWriter


## CONSTANTS & DEFINES ###

METADATA_FIELDS = [
	'identifier',
	'title',
	'description',
]



### IMPLEMEMTATION ###

class EtreeWriter (BaseWriter):
	"""
	A writer that stores ReLaIS objects as XML.

	"""
	def __init__ (self, dst, encoding='utf-8', prettyprint=False):
		"""
		Class c'tor.

		:Params:
			dst
				The ouptut point for the writer, a file path or an open and
				readable file or file-like object.
		
		"""
		BaseWriter.__init__ (self, dst, fmt='xml')
		self.encoding = encoding
		self.prettyprint = prettyprint
	
	## INTERNALS:		
	def write (self, etree_xml):
		"""
		Write an etree ELement or ElementTree to the output.

		:Params:
			etree_xml
				An etree ELement or ElementTree.
		
		"""
		# find the node at the top of the tree
		if (iselement (etree_xml)):
			assert (hasattr (etree_xml, 'tag'))
			root = etree_xml
		else:
			assert (hasattr (etree_xml, '_root'))
			root = etree_xml._root
		# if pretty-printing, indent a copy
		if (self.prettyprint):
			root = deepcopy (root)
			indent (root)
		# rewind and output, including header
		outtree = ElementTree (root)
		self.hndl.seek (0)
		self.hndl.write ("<?xml version='1.0' encoding='%s'?>\n" % self.encoding)
		outtree._write (self.hndl, root, self.encoding, {})


def write_etree (etree_xml, dst, encoding='utf-8', prettyprint=False):
	"""
	A convenience method for the quick output of etree data.
	
	:Params:
		See `EtreeWriter`.
	
	"""
	wrtr = EtreeWriter (dst, encoding, prettyprint)
	wrtr.write (etree_xml)



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
