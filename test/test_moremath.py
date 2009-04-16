#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the relais.dev.moremath module, using nose.
"""

### IMPORTS ###

from math import pi
from relais.dev import moremath


### CONSTANTS & DEFINES ###

twopi = 2 * pi
halfpi = pi / 2.0
qrtrpi = pi / 4.0


### TESTS ###

def test_mean_angle():
	m1 = moremath.mean_angle ([twopi-0.1, twopi, 0.1])
	assert (0.0 <= m1 <= 0.0001) or ((twopi - 0.0001) <= m1 <= twopi)
	m2 = moremath.mean_angle ([0.0, halfpi])
	assert ((qrtrpi - 0.0001) <= m2 <= (qrtrpi + 0.0001))

def test_mean_angle_fail():
	try:
		m1 = moremath.mean_angle ([pi, twopi])
	except:
		return
	assert (False), "this func should fail"



### END ########################################################################
