#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test the scratchfile module.
"""

### IMPORTS ###

import tempfile, os, shutil

from relais.analysis import scratchfile


### CONSTANTS & DEFINES ###

### TESTS ###

class test_scratchfile (object):
	"""
	Test the scratchfile module.
	
	For many of these functions, most assertions are carried out inside the
	actual function.
	
	"""
	testdir = 'test/out/test_scratch_file'
	copydir = 'test/in'
	
	def setUp (self):
		# make dir for testing
		os.mkdir (self.testdir)
		assert (os.path.exists (self.testdir))		
		
	def tearDown (self):
		shutil.rmtree (self.testdir)
		assert (not os.path.exists (self.testdir))
	
	def test_make_scratch_dir (self):
		"""Make a scratch dir."""
		# most assertions are carried out in actual function
		d = scratchfile.make_scratch_dir()
		assert (d.startswith (tempfile.tempdir))

	def test_make_scratch_file_1 (self):
		"""Make a scratch file in the tempdir"""
		## Preparations:
		new_file = 'foo.txt'
		## Main:
		f = scratchfile.make_scratch_file (new_file)
		assert (f.startswith (tempfile.tempdir))
		assert (f.endswith ('foo.txt'))
		assert (not os.path.exists (f))
		outfile = open (f, 'w')
		outfile.write ("bar")
		outfile.close()
		assert (os.path.exists (f))
		os.remove (f)

	def test_make_scratch_file_2 (self):
		"""Make a scratch file in a supplied dir"""
		## Preparations:
		new_file = 'foo.txt'
		new_dir = 'test_make_scratch_file_2'
		scratch_dir = os.path.join (self.testdir, new_dir)
		os.mkdir (scratch_dir)
		## Main:
		f = scratchfile.make_scratch_file (new_file, scratch_dir)
		assert (f.startswith (scratch_dir))
		assert (f.endswith (new_file))
		assert (not os.path.exists (f))
		outfile = open (f, 'w')
		outfile.write ("bar")
		outfile.close()
		assert (os.path.exists (f))
		
	def test_make_scratch_files_1 (self):
		"""Make scratch files in the tempdir"""
		## Preparations:
		new_dir = 'test_make_scratch_files_1'
		scratch_dir = os.path.join (self.testdir, new_dir)
		filenames = ['foo', 'bar', 'baz']
		## Main:
		paths = scratchfile.make_scratch_files (filenames)
		assert (len (paths) == len (filenames))
		for i, item in enumerate (paths):
			assert (item.startswith (tempfile.tempdir))
			assert (item.endswith (filenames[i]))
			assert (not os.path.exists (item))
			outfile = open (item, 'w')
			outfile.write ("blurgh")
			outfile.close()
			assert (os.path.exists (item))
			os.remove (item)

	def test_make_scratch_files_2 (self):
		"""Make scratch files in a supplied dir"""
		## Preparations:
		new_dir = 'test_make_scratch_files_2'
		scratch_dir = os.path.join (self.testdir, new_dir)
		filenames = ['foo', 'bar', 'baz']
		os.mkdir (scratch_dir)
		## Main:
		paths = scratchfile.make_scratch_files (filenames, scratch_dir)
		assert (len (paths) == len (filenames))
		for i, item in enumerate (paths):
			assert (item.startswith (scratch_dir))
			assert (item.endswith (filenames[i]))
			assert (not os.path.exists (item))
			outfile = open (item, 'w')
			outfile.write ("blurgh")
			outfile.close()
			assert (os.path.exists (item))
			os.remove (item)

	def test_recursive_remove_1 (self):
		"""Recursive removal of directory"""		
		## Preparations:
		new_dir = 'test_recursive_remove_1'
		rem_dir = os.path.join (self.testdir, new_dir)
		shutil.copytree (self.copydir, rem_dir)
		assert (os.path.exists (rem_dir))
		## Main:
		scratchfile.recursive_remove (rem_dir)
		assert (not os.path.exists (rem_dir))

	def test_recursive_remove_2 (self):
		"""Recursive removal of file"""		
		## Preparations:
		new_file = 'test_recursive_remove_2'
		new_file = os.path.join (self.testdir, new_file)
		shutil.copyfile ('test/__init__.py', new_file)
		assert (os.path.exists (new_file))
		## Main:
		scratchfile.recursive_remove (new_file)
		assert (not os.path.exists (new_file))		

	def test_recursive_clear (self):
		"""Recursive clearing of directory"""		
		## Preparations:
		new_dir = 'test_recursive_clear'
		rem_dir = os.path.join (self.testdir, new_dir)
		shutil.copytree (self.copydir, rem_dir)
		assert (os.path.exists (rem_dir))
		## Main:
		scratchfile.recursive_clear (rem_dir)
		assert (os.path.exists (rem_dir))
		assert (not os.listdir (rem_dir))


### END ########################################################################
