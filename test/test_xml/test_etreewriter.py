#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the relais.core.io.writers.etreewriter, using nose.
"""

### IMPORTS ###

from relais.dev.xml import etreewriter
from relais.dev.xml.etree import *


### CONSTANTS & DEFINES ###

### TESTS ###

class test_etreewriter1 (object):
	def setUp (self):
		self.etree = Element ('root')
		SubElement (self.etree, 'foo')
		SubElement (self.etree, 'bar', abc='123', defg='345')
		subelem = SubElement (self.etree, 'baz')
		SubElement (subelem, 'ein')
		SubElement (subelem, 'zwei')
		
	def test_write_element (self):
		src = 'test/out/io/writers/etreewriter_write_element.xml'
		wrtr = etreewriter.EtreeWriter (src)
		wrtr.write (self.etree)
		
	def test_write_tree (self):
		src = 'test/out/io/writers/etreewriter_write_tree.xml'
		wrtr = etreewriter.EtreeWriter (src)
		tree = ElementTree (self.etree)
		wrtr.write (tree)

	def test_write_encoding (self):
		src = 'test/out/io/writers/etreewriter_write_encoding.xml'
		wrtr = etreewriter.EtreeWriter (src, encoding='us-ascii')
		wrtr.write (self.etree)
		
	def test_write_direct (self):
		src = 'test/out/io/writers/etreewriter_write_direct.xml'
		wrtr = etreewriter.write_etree (self.etree, src, encoding='us-ascii')
			
	def test_write_pretty (self):
		src = 'test/out/io/writers/etreewriter_write_pretty.xml'
		wrtr = etreewriter.EtreeWriter (src, prettyprint=True)
		wrtr.write (self.etree)
			

### END ########################################################################
