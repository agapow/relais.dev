#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the relais.dev.const, using nose.
"""

### IMPORTS ###

from relais.dev import const


### CONSTANTS & DEFINES ###

### TESTS ###

def test_creation():
	const.foo = 23
	
def test_reassignment():
	const.bar = 23
	try:
		const.bar = 24
		assert (False), "should fail on reassignment"
	except:
		pass
	
def test_del():
	const.baz = 23
	try:
		del const.baz
		assert (False), "should fail on deletion"
	except:
		pass


### END ########################################################################
