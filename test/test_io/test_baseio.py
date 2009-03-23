#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the relais.dev.io.baseio, using nose.
"""

### IMPORTS ###

from StringIO import StringIO

from relais.dev.io import baseio


### CONSTANTS & DEFINES ###

### TESTS ###

class test_baseio_ctor (object):
	
	def test_filepath_ctor (self):
		src = 'test/in/dummy.jpg'
		wrtr = baseio.BaseIO (src, 'rb')
		assert (wrtr.fmt == 'jpg')
		
	def test_filehndl_ctor (self):
		src = 'test/in/dummy.jpg'
		hndl = open (src, 'rb')
		wrtr = baseio.BaseIO (hndl)
		assert (wrtr.fmt == 'jpg')

	def test_buffer_ctor1 (self):
		try:
			src = StringIO()
			wrtr = baseio.BaseIO (src)
			assert (False), "should fail as needs format"
		except:
			pass

	def test_buffer_ctor2 (self):
		src = StringIO()
		wrtr = baseio.BaseIO (src, fmt='TXT')
		assert (wrtr.fmt == 'txt')


### END ########################################################################
