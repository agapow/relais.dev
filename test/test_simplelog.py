#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the relais.dev.simplelog module, using nose.
"""

### IMPORTS ###

from relais.dev import simplelog


### CONSTANTS & DEFINES ###

### TESTS ###

def test_defaultlog():
	"""
	Test the simplest case of logging.
	"""
	lgr = simplelog.make_logger()
	lgr.info ("what?")
	
def test_filelog():
	"""
	Test logging to file.
	"""
	lgr = simplelog.make_logger (handler='test/out/test.log')
	lgr.info ("what?")

def test_debuglog():
	"""
	Test debug logging.
	"""
	lgr = simplelog.make_debug_logger (handler='test/out/test.log')
	lgr.info ("what?")

def test_daemonlog():
	"""
	Test daemon logging.
	"""
	lgr = simplelog.make_daemon_logger ()
	lgr.info ("what?")
		
def test_retrievelog():
	"""
	Test getting log by name.
	"""
	lgr = simplelog.make_logger (name='mytestlog')
	lgr.info ("what?")
	import logging
	lgr2 = logging.getLogger ('mytestlog')
	assert (lgr == lgr2), "loggers are not identical"


### END ########################################################################
