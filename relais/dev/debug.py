#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Debug and error reporting functions.

In the large, these are variants on "printf", simple functions to be be used
in debugging for dumping values to output.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import sys, traceback, os.path

__all__ = [
	'MSG',
	'msg',
	'get_call_locn',
	'get_call_locn_str',
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###########################################################

def MSG (*args, **kwargs):
	"""
	A crude 'printf' style debugging statement.
	
	:Parameters:
		args
			Values to be printed out 'as-is', rendered as strings.
		kwargs
			Values to be printed out as key-value pairs.
			
	This crudely dumps its arguments to output, allowing simple but useful
	"diagnostic printf" functionality. Un-named arguments are just printed,
	while keyworded arguments are printed with the name of the keyword. This
	is all preceded by the file, function name and line number from where it
	was called.
	
	Naturally, an error will result if an argument cannot be converted to a
	string. Note that this function is named in uppercase so it will standout
	as an obvious debug function that should be excised from production code.
	
	Call this function like::
	
		debug.MSG ("The values are", p, q, r)
		debug.MSG ("The range is from %s-%s" % (min(x), max(x)))
		debug.MSG ("fred",f="dfsdfds",terd=1)
		
	"""
	sys.stderr.write ("DEBUG (%s): %s%s\n" % (
			get_call_locn_str (-3),
			' '.join (map (str, args)),
			' '.join (map (lambda a: a+"="+str(kwargs[a]), kwargs.keys()))
		)
	)


msg = MSG


def get_call_locn (level=1):
	"""
	Return information about where this function was called from.
	
	:Parameters:
		level
			How many frames to look back in the stack for the calling frame.
	
	:Returns:
		A tuple *(<calling file path>, <line number in file>, <function name>, 
		<text of calling line>)*.
		
	"""
	# NOTE: previously, we used a negative level number. This fixes this.
	level = abs (level)
	file_path, line_no, fn_name, text = traceback.extract_stack()[-level]
	if (fn_name == '?'):
		fn_name = ''
	if (file_path != '<interactive input>'):
		file_path = os.path.basename (file_path)
	return file_path, line_no, fn_name, text


def get_call_locn_str (level=-1):
	"""
	Return information about where this function was called from.
	
	:Parameters:
		level
			How many frames to look back in the stack for the calling frame.
	
	:Returns:
		A string of form *<calling file path>:<line number>:<function name>*.
		
	"""
	# NOTE: see `get_call_locn`.
	level = abs (level) + 1
	file_path, line_no, fn_name, text = get_call_locn (level)
	return "%s:%s:%s" % (file_path, fn_name, line_no)



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
