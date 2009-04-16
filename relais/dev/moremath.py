#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Additional mathematical functions.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import math

__all__ = [
	'mean_angle',
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def angle (pt1, pt2):
	"""
	Give the angle (bearing) from one point to another.
	
	:Parameters:
		pt1, pt2
			2D coordinates, with x and y in indices 0 and 1.
		
	:Returns:
		The bearing in radians.
		
	A ridiculously simple function, but useful for readability.
	"""
	# calced as atan2(deltay,deltax)
	return math.atan2 (pt2[1]-pt1[1], pt2[0]-pt1[0])


def mean_angle (angles, sensitivity=1e-12):
	"""
	Return the mean angle of those passed.
	
	:Parameters:
		angles
			An iterable of angles measured in radians.
			
	:Returns:
			The mean angle in positive radians.
			
	Calculating the mean of a series of angles is difficult, given the "wrap
	around" measurement of angles. The average of 85 and 95 degrees is 90,
	but the average of 355 and 5 degrees is 180. This function solves the
	problem via complex math. Note that there are still ambiguous cases (i.e.
	what the average of 90 and 270 degrees?). The sensitivity argument should
	catch most of those (if the angles are too opposite), but we advise this
	should only be used where it is known there will be a clear answer.
	
	From J.A. Dunne's Matlab implementation.
	
	"""
	## Preconditions & trivial cases:
	if (len (angles) == 1):
		return angles[0]
	## Main:
	import math, cmath
	x = [cmath.exp (1j * x) for x in angles]
	mean = sum (x) / len (x)
	assert (sensitivity < abs (mean))
	res = math.atan2 (mean.imag, mean.real)
	if (res < 0):
		res = 2 * math.pi + res
	## Postconditions & return:
	return res
	
	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ######################################################################
