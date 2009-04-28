#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test the clineapp module.
"""

### IMPORTS ###

import tempfile, os, shutil

from relais.analysis import clineapp


### CONSTANTS & DEFINES ###

### TESTS ###

def test_find_exe_1():
	x = clineapp.find_exe ('perl')
	assert (x == '/opt/local/bin/perl')

def test_find_exe_1():
	x = clineapp.find_exe ('/opt/local/bin/perl')
	assert (x == '/opt/local/bin/perl')
		
def test_find_exe_3():
	x = clineapp.find_exe ('notaprogram')
	assert (x is None)
		

class test_clineapp (object):
	"""
	Test the clineapp module.
	
	For many of these functions, assertions are carried out inside the
	actual function.
	
	"""
	testdir = 'test/out/test_clineapp'
	
	def setUp (self):
		# make dir for testing
		os.mkdir (self.testdir)
		assert (os.path.exists (self.testdir))		
		
	def tearDown (self):
		shutil.rmtree (self.testdir)
		assert (not os.path.exists (self.testdir))
		
	def test_clineapp_ctor (self):
		# try various ctor variations
		c1 = clineapp.ClineApp ('perl')
		
		c2 = clineapp.ClineApp ('perl', use_workdir=False)	
		
		workdir = os.path.join  (self.testdir, 'test_clineapp_ctor1')
		os.mkdir (workdir)
		c3 = clineapp.ClineApp ('perl', use_workdir=True, workdir=self.testdir)	
		
		c4 = clineapp.ClineApp ('perl', use_workdir=True)	
		
		# this generates a warning when the incomplete object is disposed of	
		try:
			workdir = os.path.join  (self.testdir, 'test_clineapp_ctor2')
			os.mkdir (workdir)
			c5 = clineapp.ClineApp ('perl', use_workdir=False,
				workdir=self.testdir)
			assert (False), "this ctor should fail"
		except:
			pass
		
		# this generates a warning when the incomplete object is disposed of	
		try:
			c5 = clineapp.ClineApp ('perl', use_workdir=False,
				remove_workdir=True)
			assert (False), "this ctor should fail"
		except:
			pass
			
	def test_clineapp_setup_workdir (self):
		# try various ctor variations
		c1 = clineapp.ClineApp ('perl')
		c1.setup_workdir()
		workdir = c1._curr_workdir
		assert (workdir)
		assert (workdir.startswith (tempfile.tempdir))
		assert (not c1.workdir)
		assert (os.path.exists (workdir))
		del c1
		assert (os.path.exists (workdir))

		c2 = clineapp.ClineApp ('perl', remove_workdir=True)
		c2.setup_workdir()
		workdir = c2._curr_workdir
		assert (workdir)
		assert (workdir.startswith (tempfile.tempdir))
		assert (not c2.workdir)
		assert (os.path.exists (workdir))
		del c2
		assert (not os.path.exists (workdir))
				
		c3 = clineapp.ClineApp ('perl', use_workdir=False)	
		c3.setup_workdir()
		assert (not c3._curr_workdir)
		assert (not c3.workdir)
		
		c1 = clineapp.ClineApp ('perl', use_workdir=True)
		c1.setup_workdir()
		workdir = c1._curr_workdir
		assert (workdir)
		assert (workdir.startswith (tempfile.tempdir))
		assert (not c1.workdir)
		assert (os.path.exists (workdir))
		del c1
		assert (os.path.exists (workdir))

		c2 = clineapp.ClineApp ('perl', use_workdir=True, remove_workdir=True)
		c2.setup_workdir()
		workdir = c2._curr_workdir
		assert (workdir)
		assert (workdir.startswith (tempfile.tempdir))
		assert (not c2.workdir)
		assert (os.path.exists (workdir))
		del c2
		assert (not os.path.exists (workdir))

	def test_clineapp_build_cmdline (self):
		c1 = clineapp.ClineApp ('perl')
		line = c1._build_cmdline()
		assert (line.startswith ("cd %s" % tempfile.tempdir))
		assert (line.endswith ("; perl"))
		
		c2 = clineapp.ClineApp ('perl', use_workdir=False)	
		line = c2._build_cmdline()
		assert (line == 'perl')
		
		c3 = clineapp.ClineApp ('perl', use_workdir=False)	
		line = c3._build_cmdline ('-h', '--foo 23', 'bar')
		assert (line == 'perl -h --foo 23 bar')

	def test_clineapp_call_1 (self):
		c = clineapp.ClineApp ('ls', use_workdir=False)	
		c.call_cmdline ('test/in/dummy')
		print '.%s.%s.%s.' % (c.cline_err, c.cline_out, c.cline_status)
		assert (not c.cline_err)
		assert (c.cline_out == 'bar\nbaz\ndummy2\nfoo\n')
		assert (c.cline_status == 0)
			
	def test_clineapp_call_2 (self):
		c = clineapp.ClineApp ('ls', use_workdir=False)	
		c.call_cmdline ('nosuchdir')
		assert (c.cline_err.startswith ('ls: nosuchdir: No such file or directory'))
		assert (c.cline_out == '')
		assert (1 < c.cline_status)



### END ########################################################################
