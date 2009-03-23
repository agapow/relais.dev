#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A connection for transferring files via FTP.

While the standard library has FTP capabilities, these are thinly documented,
obscure and raw. (To some extent, this is because it is based on the basal FTP
protocol, not the user-end.) This module serves as a (thin) wrapper around
the standard FTP functions, both to simplify and illustrate its use and to
provide some useful functionality.

An equivalent module for SFTP would be useful, but would involve using the
third-party paramiko and pycrypto libraries.

"""
# TODO: can we log in from a timed-out connection?
# TODO: better way to handle faulty 'dir'?

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from ftplib import FTP


#__all__ = [
#	'TagAttrib',
#]


### CONSTANTS & DEFINES ###

BINARY_MODES = [
	'binary',
	'bin',
	'b',
]

TEXT_MODES = [
	'text',
	't',
	'ascii',
]


### IMPLEMENTATION ###

class FtpCnxn (object):
	"""
	An FTP connection with file transfer capabilities.
	
	For example::
	
		>>> c = FtpConnection ("www.viedigitale.com", "viedigit", "jiIpq2")
		>>> c.dir()
		
	"""
	
	## Lifecycle:
	def __init__ (self, host, user=None, passwd=None):
		"""
		Initiate a connection to the remote host.
		
		:Params:
			host string
				The remote server name.
			user string
				The login name (if required).
			passwd string
				The login password (of required).
				
		Usually, opening a connection will require a username and password but
		if need be a connection can be opened neither or with only a username.
		Note that if a connection is refused, an exception will probably be
		thrown and you will end up with a non-functi
		
		"""
		## Preconditions:
		assert (host)
		## Main:
		if (passwd):
			self._conn = FTP (host, user, passwd)
		elif (user):
			self._conn = FTP (host, user)
		else:
			self._conn = FTP (host)
			
	def __del__ (self):
		"""
		Close and delete the connection.
		
		Note that in some circumstances (e.g. session termination), Python
		objects are deleted untidily, leading to exceptions being raised when
		this is called.
		
		"""
		self._conn.close()
		
	## Accessors:
	def dir (self, patt=''):
		"""
		List all items in the remote directory, or those that match a pattern.
		
		:Params:
			patt string
				What glob pattern, if any, to match file names against.
				
		This corresponds to the conventional FTP command ``dir``.  Note that it
		will return directories as well. If an asterisk is passed in as the
		pattern, it will recurse into directories.
		
		"""
		try:
			return self._conn.nlst (patt)
		except:
			return []
		
	ls = dir
	
	def pwd (self):
		return self._conn.pwd()
		
	## Mutators:
	def cwd (self, newdir):
		self._conn.cwd (newdir)
		
	def get_file (self, filename, outfile=None, mode='b'):
		"""
		Download files from the remote host.
		"""
		## Preconditions & preparation:
		# determine mode
		if (mode.lower() in BINARY_MODES):
			mode = 'b'
		elif (mode.lower() in TEXT_MODES):
			mode = 't'
		else:
			assert (false), "mode '%s' is not recognised" % mode
		# if no outfile, create a similar name to source
		if (outfile is None):
			outfile = filename
		# if outfile is a filepath, open it
		if (not hasattr (outfile, 'write')):
			opened_file = True
			if (mode is 'b'):
				outfile = open (outfile, 'wb')
			else:
				outfile = open (outfile, 'w')
		else:
			opened_file = False
		## Main:
		if (mode is 'b'):
			self.get_binary (filename, outfile)
		else:
			self.get_text (filename, outfile)
		## Postconditions & closure:
		if (opened_file):
			outfile.close()
		
	def mget_file (self, patt, mode='b'):
		filelist = self.dir (patt)
		for f in filelist:
			self.get_file (f, f, mode)
			
	def remove (self, fname):
		self._conn.delete (fname)
			
	## INTERNALS
	def get_text (self, filename, outfile):
		"""
		Borrowed from Frederick Lundh.
		"""
		self._conn.retrlines ("RETR " + filename,
			lambda s, w=outfile.write: w (s+"\n"))
			
	def get_binary (self, filename, outfile):
		self._conn.retrbinary ("RETR " + filename, outfile.write)
	


### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ###################################################################
