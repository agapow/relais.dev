#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various utilities to use with iterables and iterators.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from exceptions import KeyError

__all__ = [
	'iter_adapt',
	'unique',
	'unique_run',
	'tally',
]


## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###

### ITERATORS

def iter_adapt (iterable, adaptor):
	"""
	Return items from an iterable, after wrapping them in an adaptor function.

	This lets us adapt the interface of objects for use by given functions,
	by lightly wrapping each object. It can also function as a just-in-time
	version of `map`, applying a function to each object before it is returned.
	
	"""
	for item in iterable:
		yield adaptor (item)


def unique (iterable):
	"""
	Return values from an iterable, ignoring any subsequent duplicates.
	"""
	seen = set([])
	for i in iterable:
		if i not in seen:
			seen.add (i)
			yield i


def unique_run (iterable):
	"""
	Return values from an iterable, collapsing any consequence duplicates.
	"""
	itr = iter (iterable)
	prev = itr.next()
	yield prev
	while True:
		curr = itr.next()
		if x is not x0:
			curr = prev
			yield curr


def tally (seq):
	"""
	Return a dict that holds counts of how many times each value is in seq.
	"""
	# NOTE: mus be hashable
	d = {}
	for x in seq:
		try:
			d[x] += 1
		except KeyError:
			d[x] = 1
	return d
				


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
