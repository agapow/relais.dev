#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple mountpoint / plugin implementation.

Lifted from Marty Alkchin and "Pro Django".

"""
# NOTE: 20071125 tested and passed.

__docformat__ = 'restructuredtext en'


### IMPORTS ###

__all__ = [
	'Mountpoint'
]


## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###

class Mountpoint (type):
	"""
	A simple mountpoint / plugin implementation.
	
	Mountpoint classes should be declared::
	
		class MyMountpt (object):
			__metaclass__ = Mountpoint
			
	and mountpoints of that class can be defined as normal::
	
		class Plain (MyMountpt):
			...
			
		class Fancy (MyMountpt):
			...
			
	The base class can be queried for what classes implement it::
	
		for item in MyMountpt.plugins:
			plugin_inst = item()
	
	"""
	def __init__(cls, name, bases, attrs):
		if not hasattr (cls, 'plugins'):
			# This branch only executes when processing the mount point itself.
			# So, since this is a new plugin type, not an implementation, this
			# class shouldn't be registered as a plugin. Instead, it sets up a
			# list where plugins can be registered later.
			cls.plugins = []
		else:
			# This must be a plugin implementation, which should be registered.
			# Simply appending it to the list is all that's needed to keep
			# track of it later.
			cls.plugins.append (cls)
		if (hasattr (cls, '__init_cls__')):
			cls.__init_cls__()
		
	def get_plugins (self, *args, **kwargs):
		"""
		Return the instatiated plugins of this class.
		"""
		return [p(*args, **kwargs) for p in self.plugins]

### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod()


### MAIN ###

if __name__ == '__main__':
	_doctest()


### END ########################################################################
