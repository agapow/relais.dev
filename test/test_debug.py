#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the relais.dev.debug, using nose.
"""

### IMPORTS ###

from relais.dev import debug


### CONSTANTS & DEFINES ###

### TESTS ###

def test_msg():
	assert (debug.MSG == debug.msg)
	p, q, r = 4, 'foo', ['b', 'a', 'r']
	# TODO: unsure how I best can test printing statements
	



### END ########################################################################
