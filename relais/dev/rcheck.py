#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Runtime checks and assertions.

These include type-testing (e.g. "is this object like a list?") and a variety of
assertion variants

"""
# NOTE: 20071125 tested and passed.

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import warnings
import exceptions
import types
import os

from relais.dev import debug

__all__ = [

]


## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###

### TYPE TESTING

def is_sequence (obj):
	"""
	Is this object a list or tuple?

	A wider variety of sequence types could be accomodated, but it is difficult
	to distingush their signature from dictionaries, so this currently only
	detects the two canonical sequence types.
	
	"""
	return (type (obj) in (types.ListType, types.TupleType))


def make_sequence (obj):
	"""
	If this object is not a sequence, make it one.

	This is used for functions that can accept a single instance or sequence of
	object, converting instances to a list of one. It's called 'make_sequence'
	rather than 'make_list' because tuples pass through unchanged.
	
	"""
	# NOTE: we make a list by enclosing it in square braces. If you were to
	# use the function `list()`, it would convert a string into a list of 
	# characters, e.g. ['f', 'o', 'o']
	if (is_sequence (obj)):
		return obj
	else:
		return [obj]


### ASSERTIONS

def assert_file_exists (file_path):
	"""
	Check that a file exists at the given location.
	"""
	assert (type (file_path) == type ('')), \
		"file path is type %s" % type (file_path)
	assert (os.path.isfile (file_path)), \
		"file '%s' doesn't exist" % file_path


def assert_val_equal (var, allowed_vals):
	"""
	Test to see if a variable is equal to one a set of allowed values.

	Note that this tests on equality: '5' is equal to 5.0. But in this case,
	'5' doesn't equal True, nor is '' equal to False or vice versa.

	For example::

		>>> val = 5
		>>> assert_val_equal (val, [5])
		>>> assert_val_equal (val, ['a', 4, 5])
		>>> assert_val_equal (val, [5.0])
		>>> assert_val_equal (val, ['z', 6])
		Traceback (most recent call last):
		...
		AssertionError: found '5', expected one of '['z', 6]'


	"""
	assert (var in make_sequence (allowed_vals)), \
		"found '%s', expected one of '%s'" % (var, allowed_vals)


def assert_val_is (var, allowed_vals):
	"""
	Test to see if a variable is in a list of allowed values.

	This functions as a stricter version of `assert_val_equal`, in that it
	tests for 'is' instead of 'equal', and thus will avoid (say) any conversion
	problems between ints andfloats.

	For example::

		>>> val = 5
		>>> assert_val_is (val, [5])
		>>> assert_val_is (val, ['a', 4, 5])
		>>> assert_val_is (val, [5.0])
		Traceback (most recent call last):
		...
		AssertionError: found '5', expected one of '[5.0]'


	"""
	assert ([x for x in make_sequence (allowed_vals) if (x is var)]), \
		"found '%s', expected one of '%s'" % (var, allowed_vals)


def assert_vals_in (var, allowed_vals):
	"""
	Test to see if a variable (or variables) is in a set of allowed values.

	"""
	var = make_sequence (var)
	allowed_vals = make_sequence (allowed_vals)
	for v in var:
		assert (v in allowed_vals), "'%s' not in '%s'" % (v, allowed_vals)
				

def assert_type (var, allowed_types):
	"""
	Test to see if a variable is of a set of allowed types.

	For example::

		>>> val = 5
		>>> from types import IntType, StringType, FloatType
		>>> assert_type (val, [IntType])
		>>> assert_type (val, [StringType, IntType, FloatType])
		>>> assert_type (val, [StringType, FloatType])
		Traceback (most recent call last):
		...
		AssertionError: found '5' of type '<type 'int'>', expected one of [<type 'str'>, <type 'float'>]

	"""
	assert (type (var) in make_sequence (allowed_types)), \
		"found '%s' of type '%s', expected one of %s" % (var, type (var),
		allowed_types)


def assert_type_like (var, allowed_types):
	"""
	Test to see if a variable is the same type as one of a set of values.

	For example::

		>>> val = 5
		>>> assert_type_like (val, [10])
		>>> assert_type_like (val, ['a', 10, 5.0])
		>>> assert_type_like (val, ['a', 5.0])
		Traceback (most recent call last):
		...
		AssertionError: found '5' of type '<type 'int'>', expected one of [<type 'str'>, <type 'float'>]


	"""
	assert_type (var, [type (x) for x in make_sequence (allowed_types)])


def assert_in_bounds (var, lower, upper):
	"""
	Test to see if a variable falls within a pair of inclusive bounds.

	For example::

		>>> val = 5
		>>> assert_in_bounds (val, 0, 10)
		>>> assert_in_bounds (val, 5, 10)
		>>> assert_in_bounds (val, 0, 5)
		>>> assert_in_bounds (val, 5, 5)
		>>> assert_in_bounds (val, 6, 10)
		Traceback (most recent call last):
		...
		AssertionError: '5' is less than lower bound '6'
		>>> assert_in_bounds (val, 0, 4)
		Traceback (most recent call last):
		...
		AssertionError: '5' is greater than upper bound '4'

	"""
	assert (lower <= var), "'%s' is less than lower bound '%s'" % (var, lower)
	assert (var <= upper), "'%s' is greater than upper bound '%s'" % (var, upper)


def failure (msg=None):
	"""
	Raises an assertion where you get somewhere you shouldn't have.
	"""
	final_msg = "shouldn't get here"
	if (msg):
		final_msg += ': ' + msg
	assert (False), final_msg


### WARNINGS & LOGGING

def warn_deprecated (msg='deprecated'):
	called_from = debug.get_call_locn_str (-3)
	warnings.warn ("%s %s" % (called_from, msg), DeprecationWarning)


def runtime_warning (msg):
	called_from = debug.get_call_locn_str (-3)
	warnings.warn ("%s %s" % (called_from, msg), RuntimeWarning)



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
