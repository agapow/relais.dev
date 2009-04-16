#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Functions for creating temporary files.

This wraps and enhances the facilities of the standard ``tempfile`` library,
mostly for the purposes of calling external applications and writing data
to scratch files. It time it will probably move to relais.core.utils.

The name, while awkward, serves to disintinguish it from the standard library.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import exceptions
import tempfile
import os
import sys
import shutil


## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###

def make_scratch_dir ():
	"""
	Create a temporary directory and return it's path.

	This is intended for when you are using the temporary directory to create
	create files with fixed names, and you want to avoid the possibility of
	colliding with other files or processes. The solution is to create a
	temporary directory and do all your work in there.

	"""
	# TODO: a 'temporary workspace' class that cleans up after itself?
	# See TemporaryFile in tempfile
	# TODO: allow the designation of a scratch area?
	## Main:
	tmp_path = tempfile.mktemp()
	os.mkdir (tmp_path)
	## Postconditions & return:
	assert (os.path.exists (tmp_path)), "can't create temporary directory"
	return tmp_path


def make_scratch_file (file_name, scratch_dir=None):
	"""
	Make a temporary file of the name given.

	This is intended for those cirumstances where the name of the file is fixed
	and so ``tempfile`` cannot be used directly because of name collision. If 
	a temporary directory is specified, the file will be be created there.
	otherwise a temporary directory (of random name) will be created.
	
	Note that like the ``tempfile`` functions, this does not create the actual
	file, just generating a path for the file to be created at and ensuring
	that the path is legal.
	
	:Parameters:
		filename
			The name of the file name to create.
		temp_dir
			The path of a directory to create the file in.

	:Returns:
		A file path.

	"""
	if (scratch_dir is None):
		scratch_dir = make_scratch_dir()
	new_path = os.path.join (scratch_dir, file_name)
	assert (not os.path.exists (new_path)), \
			"path '%s' already exists" % new_path
	return new_path


def make_scratch_files (file_names, scratch_dir=None):
	"""
	Make several temporary files of the names given.
	
	This just serves as an convenient way to call ``make_scratch_file`` for
	multiple files.

	:Parameters:
		filenames
			Sequence of file names.
		scratch_dir
			See ``make_scratch_file``.

	:Returns:
		A list of file paths. 

	"""
	if (scratch_dir is None):
		scratch_dir = make_scratch_dir()
	file_paths = []
	for item in file_names:
		file_paths.append (make_scratch_file (item, scratch_dir))
	return file_paths


def write_handle_to_tmpfile (data_hndl, file_name=None, file_suffix=None):
	"""
	Write data to a temporary file of the given name and return the path.

	As several functions in ReportLab, BioPython and other modules require
	actual filepaths for initialisation and we are dealing with file objects or
	data in memory, it becomes necessary to write the data down to disk
	temporarily so it can be read back up.

	Note that if an exact filename is given, it will be created in a temporary
	directory for safety. See `make_tmp_dir`.

	:Parameters:
		data_hndl
			An open file or file-like object (with 'read()').
		file_name
			The name of the temporary file to be created. If not provided, one
			will be generated.
		file_suffix
			If no file name is provided, teh one generated will have this suffix.

	:Returns:
		The path to the newly created file.

	"""
	# TODO: need file mode?
	## Preconditions:
	# can't have file name and suffix
	
	## Main:
	if (file_name):
		file_path = make_scratch_file (file_name)
	elif (file_suffix):
		file_path = tempfile.mktemp (file_suffix)
	out_file = open (file_path, 'wb')
	out_file.write (data_hndl.read())
	out_file.close()
	## Postconditions & return:
	return file_path


def recursive_remove (path):
	"""
	Given a path, delete that file or folder and any contents.

	Use with care. This essentially duplicates ``rm -r``, deleting a non-empty
	directory. It largely duplicates certain standard library functions
	(except for being able to acccept a file) and is here for completeness
	(match with ``recursive_clear``) and because of historical reasons.

	:Parameters:
		path
			Path to the file or directory to be removed.

	"""
	# TODO: there *must* be a standard function for this. os.removedirs()?
	## Preconditions:
	assert (os.path.exists (path))
	## Main:
	if os.path.isfile (path):
		os.remove (path)
	elif os.path.isdir (path):
		shutil.rmtree (path)


def recursive_clear (path):
	"""
	Delete the contents of a directory, while leaving the directory itself.
	
	This duplicates ``recursive_remove`` except that a directory - not a file -
	must be supplied and the directory itself is left intact.
	"""
	## Preconditions:
	assert (os.path.exists (path) and os.path.isdir (path))
	## Main:
	contents = os.listdir (path)
	for item in contents:
		new_path = os.path.join (path, item)
		recursive_remove (new_path)


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
