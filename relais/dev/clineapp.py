#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Calling and retrieving information from external commandline applications.

It's often necessary to call complicated external programs that may require
some setup (e.g. parameters, input files, being called from a set location)
and teardown (e.g. processing output files, cleaning up temporary data). This
module provides a base class that provides a structured way to handle such
situations.

Caveats: This calls the external commandline and waits for it to finish. There
is no sophisticated job control and thus calling processes may get hungup
waiting for the commandline to complete.

While there's some half-hearted support for Windows, at the moment this is
focused on Unix-like environments.

Beware when passing in working directories and setting them to be deleted. Is
this really what you intended? Often it's safer to use the default behaviour
and leave the directory, especially if it is auto-created in /tmp.

It's not intended that this class be used for multiple commandline calls,
although there is nothing preventing this and it may even make sense in some
cases.

In situations where complex setup (or cleanup) is required, subclassing would
be appropriate.

"""
#TODO: should be reimplemented using subprocess

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import os, commands, popen2, sys, exceptions, subprocess, signal

from common import *
import scratchfile

__all__ = [
	'ClineApp'
]


## CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class ClineApp (object):
	"""
	An encapsulation of commandline application usage.
	
	This class calls external commandlime executables, with successive methods
	setting up the environment for the commandline, doing the actual call, and
	recovering output and any produced files. For example, the below code
	will prepare to execute ``myexe`` in ``home/mydir``, after checking the
	program requirements. It then calls ``myexe -a foo -b bar c=baz``. After
	completion, output data is recovered. When the ``clapp`` object is
	deleted, cleanup of the work directory is triggered::
	
		clapp = ClineApp ('myexe', use_workdir=True, workdir='home/mydir',
			remove_workdir=True, check_requirements=True)
		clapp.call_cmdline ('-a', 'foo', '-b bar', 'c=baz')
		status = clapp.cline_status
		output = clapp.cline_out
		error_output = clapp.cline_error
		del clapp
		
	In broad detail, the class lifecycle is:
	
	* create the class, defining the executable, whether to run it in a
		working directory, supplying that directory or letting a temporary one
		be generated, whether to clean up the working directory, and whether
		to check for executable requirements.
		
	* running the commandline (executable) with a given set of arguments and
		waiting for completion.
	
	* reading out the status returned by the executable, the output it sent to
		stdout and stderr and file data produced by the commandline (all
		optionally).
		
	* cleaning up the working directory (optional)
	
	* deleting the ClineApp object, which triggers cleanup (optional)
	
	"""
	# NOTE: There may sometimes when a cleanup *within* working dir (but not
	# the dir itself), is needed
	# butnot the dir itself?
	
	def __init__ (self, exepath, use_workdir=True, workdir=None,
			remove_workdir=False, check_requirements=False):
		"""
		C'tor, specifying the behaviour of commandline when it is called.
		
		:Parameters:
			exepath : string
				The path to the executable or name by which it is invoked.
			use_workdir : boolean
				Should a working directory or scratch area be used?
			workdir : string
				The path to the working directory. If this is not supplied but
				`use_workdir` is set, a temporary directory will be created.
			remove_workdir
				If a workdir is used, should it be removed after use? Note this
				allows the removal of workdir that have been created outside
				the class and passed in.
			check_requirements
				Check prerequisites for the commandline before calling it.
			
		"""
		## Preconditions:
		# check 
		assert (isinstance (exepath, basestring)) 
		if (not use_workdir):
			assert (not remove_workdir and not workdir)
		## Main:
		self.exepath = exepath
		self.use_workdir = use_workdir
		self.workdir = workdir
		self.remove_workdir = remove_workdir
		self.check_requirements = check_requirements
		# the actual workdir & commandline used
		self._curr_workdir = self._curr_cline = None
		# the output, errors and status of the commandline
		self.cline_err = self.cline_out = self.cline_status = None
		
		
	def __del__ (self):
		"""
		D'tor for the class, which cleans up the working dir if required.
		
		This terminates the cline process if it is (apparently) still running.
		"""
		# See kill discussion at <http://objectmix.com/python/17481-subprocess-leaves-child-living.html>
		# need 'hasattr' due to Python's unruly tidying up at session deletion
		if (hasattr (self, '_proc')):
			# is the process still running? kill it
			if (self._proc.poll() is None):
				os.kill (self._proc.pid, signal.SIGTERM)
			del self._proc
		# delete tmpdir if need be
		self.cleanup_workdir()
		
	def assert_requirements (self):
		"""
		Check that the commandline can be called.
		
		This currently does nothing other than just testing that the exepath
		can be found and the working dir can be reached, throwing an exception
		if not. More complex requirements should be placed in derived classes.
		
		"""
		# TODO: check permissions of the working dir?
		path = commands.getoutput ('which %s' % self.exe_path)
		assert (not path.startswith ('no ')), \
			"can't find exepath (%s)" % path
		if (self.use_workdir):
			assert (os.path.exists (self._curr_workdir)), \
				"can't access working dir (%s)" % self._curr_workdir
		
	def call_cmdline (self, *clargs):
		"""
		Call cmdline with the given arguments.
		
		:Parameters:
			clargs
				A string or sequence of strings being commandline arguments. If
				a sequence, they are concatenated with intervening spaces.
		
		If needed, create and change to the working directory. If the necessary
		flag is set, requirements will be checked and an exception thrown if
		not met. Sublclass may provide a "run" or "run_<variant>" method (e.g.
		'run_fastjoin', 'run_assemble') for calling given sets of arguments, and
		doing any other preparation.
		
		"""
		# NOTE: pass in the args as a dict? doesn't preserve order
		## Main:
		self.setup_workdir()
		cmdline = self._build_cmdline (*clargs)
		MSG (cmdline)
		self._curr_cline = cmdline 
		# actually call commandline
		err_msg = 'Error in running external commandline. ' \
			'Perhaps a required program is not installed or inaccessible (%s).'
		try:
			# call and wait to finish
			#proc = popen2.Popen3 (cmdline, capturestderr=True)
			if (self.use_workdir):
				workdir = self._curr_workdir
			else:
				workdir = None
			self._proc = subprocess.Popen (cmdline, stdout=subprocess.PIPE,
           stderr=subprocess.PIPE, cwd=workdir, shell=True)
			self.cline_status = self._proc.wait()
			# store output and error stream
			# note that if the proc faults out, it creates neither of its streams
			#if (proc.childerr):
			#	self.cline_err = proc.childerr.read()
			#if (proc.fromchild):
			#	self.cline_out = proc.fromchild.read()
			if (self._proc.stderr):
				self.cline_err = self._proc.stderr.read()
			if (self._proc.stdout):
				self.cline_out = self._proc.stdout.read()
					
		#except exceptions.StandardError, err:
		#	raise exceptions.ValueError (err_msg % str (err))
		except:
			raise
		#	raise exceptions.ValueError (err_msg % 'unknown fault')
	
	def _build_cmdline (self, *clargs):
		"""
		Construct the commandline to be called.
		
		This is largely a convenience function and point for overriding in
		subclasses. It constructs a command line that changes to the working
		working directory, and calls the executable with the supplied arguments.
		"""
		## Main:
		# check if need be
		if self.check_requirements:
			assert (self.assert_requirements())
		# assemble the commandline
		if (clargs):
			argline = ' ' + ' '.join (clargs)
		else:
			argline = ''
		#if (self.use_workdir):
		#	prefix = "cd %s; " % self._curr_workdir
		#else:
		#	prefix = ''
		prefix = ''
		## Return:
		return "%s%s%s" % (prefix, self.exepath, argline)		
		
	def setup_workdir (self):
		"""
		Prepare the working directory.
		
		If necessary, this creates the working area. The path to it is recorded
		in the member ``_curr_working_dir``. If further preparation is required
		(e.g. writing input files for later use by the application), this method
		should be overridden, with the derived function calling this and then
		performing any further actions.
		
		Note that this function is called whether the workdir argument is
		speficied or not. This allows this function to be overridden to do
		whatever prepraration is required.
		
		"""
		if (self.use_workdir):
			self._curr_workdir = self.workdir
			if (not self._curr_workdir):
				self._curr_workdir = scratchfile.make_scratch_dir()
				
	def cleanup_workdir (self):
		"""
		If a working directory was specified and flagged for removal, remove it.
		
		This is called from the class d'tor, but can also be called explicitly
		if need be. Note that the working directory is removed whether it was
		supplied to or created by the class. Be wary of deleting directories
		you didn't mean to.
		
		Subclasses may need to override this to provide specialised cleanup.
		For example, there may be times when a cleanup *within* working dir (but
		not the dir itself), or targetting of specific files is needed.
		
		"""
		# if workdir should be removed and one is used ...
		if (self.remove_workdir and self.use_workdir):
			# if area has been created ...
			if (self._curr_workdir):
				scratchfile.recursive_remove (self._curr_workdir)
				self._curr_workdir = None
				
	def extract_diagnostics (self):
		"""
		Return any datafiles generated by the cline.
		
		:Returns:
			A dictionary of *file_name* / *file_contents* from files generated by
			the commandline in the work directory
		
		This is intended for returning file output from any run, for the
		edification of users. It should be defined by any derived class that
		requires it.
		
		"""
		raise exceptions.NotImplementedError (
			"this should be supplied by a derived class")
		
	

### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
