#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various functions for manipulating files and handles.
"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import cStringIO, os


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def string_to_handle (in_str):
	"""
	Converts a string to a suitable open handle for parsers.
	
	Note: this is like a file that has already been opened.
	"""
	return cStringIO.StringIO (in_str)


def ext_from_filepath (fpath, lower=True):
	"""
	Return the extension of this file name or path.
	
	:Parameters:
		fpath
			File name or path
		lower
			Normalise the extension to lower case.
			
	:Returns:
		The file extension, without the seperator / do character.
		
	"""
	basename, ext = os.path.splitext (fpath)
	if ext.startswith (os.extsep):
		ext = ext[len (os.extsep):]
	if (lower):
		ext = ext.lower()
	return ext

def file_to_string (path, mode='rU'):
	"""
	Reads the contents of a file and returns it as a string.

	This is a convenience method, simply for brevity.

	:Params:
		path
			The path to the file.
		mode
			The mode to use when opening and reading the file.

	:Returns:
		A string.
	"""
	## Preconditions:
	assert ('w' not in mode)
	## Main:
	fhndl = open (path, mode)
	buf = fhndl.read()
	fhndl.close()	
	return buf


def string_to_file (buf, path, mode='w'):
	"""
	Write the buffer to the given file.

	This is a convenience method, simply for brevity.

	:Params:
		buf
			The buffer or string to be written.
		path
			The path to the file.
		mode
			The mode to use when opening and writing the file.

	"""
	## Preconditions:
	assert ('r' not in mode)
	## Main:
	fhndl = open (path, mode)
	fhndl.write (buf)
	fhndl.close()
	
def hoover_dir (path, filenames=None, mode='rU'):
	"""
	Extract all the files in a given directory and return then in a dict.

	:Params:
		path
			Path to the target directory.
		filenames
			A list of files in the directory to extract. If none are provided,
			all files will be extracted.
		mode
			The mode to read files with.

	:Returns:
		A dictionary of (file-name, file-contents)

	"""
	# TODO: allow filenames to be a selector func?
	## Preconditions:
	assert (os.path.exists (path))
	assert (os.path.isdir (path))
	## Main:
	if (filenames is None):
		filenames = os.listdir (path)
	results = {}
	for f in filenames:
		fpath = os.path.join (path, f)
		assert (os.path.exists (fpath))
		if (os.path.isfile (fpath)):
			results[f] = file_to_string (fpath, mode)
	## Return:
	return results


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
	_doctest()

	
### END ###################################################################
