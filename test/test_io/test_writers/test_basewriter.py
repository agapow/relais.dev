#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the relais.dev.io.writers.basewriter, using nose.
"""

### IMPORTS ###

from StringIO import StringIO

from relais.dev.io.writers import basewriter


### CONSTANTS & DEFINES ###

### TESTS ###

class test_basewriter_ctor (object):
			
	def test_filepath_ctor (self):
		src = 'test/out/dummy.txt'
		wrtr = basewriter.BaseWriter (src)
		assert (wrtr.fmt == 'txt')

	def test_filehndl_ctor1 (self):
		src = 'test/out/dummy.txt'
		hndl = open (src, 'w')
		wrtr = basewriter.BaseWriter (hndl)

	def test_filehndl_ctor2 (self):
		src = 'test/out/dummy.txt'
		hndl = open (src)
		wrtr = basewriter.BaseWriter (hndl)
		
	def test_filehndl_ctor3 (self):
		src = 'test/out/dummy.txt'
		hndl = open (src)
		wrtr = basewriter.BaseWriter (hndl, fmt='TXT')

	def test_buffer_ctor1 (self):
		try:
			src = StringIO()
			wrtr = basewriter.BaseWriter (src)
			assert (False), "should fail as needs format"
		except:
			pass
			
	def test_buffer_ctor2 (self):
		src = StringIO()
		wrtr = basewriter.BaseWriter (src, fmt='TXT')


### END ########################################################################
