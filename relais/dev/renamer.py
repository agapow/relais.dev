#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Renaming objects to make them unique and safe.

Several functions in libraries or external programs have restrictions upon the
names or identifiers used for objects. They may silently assume that ids are
unique within a collection of objects, that names have no spaces or are less
than X characters long, or simply that objects have names or ids.
Alternatively, they may abbreviate or mangle non-conforming names such that
output data contains unrecognizable or duplicate names. For example, several
functions or programs called by Biopython (e.g. Clustal) expect continuous
alphanumerics of 16 characters or less. The result is that functions error out
or deliver confusing results.

To this end, this package contains facilities for generating simple unique
names, translating problematic names into safe forms and later back
translating them.

Note: be careful when renaming objects that are persisted from a database (e.g.
via SqlAlchemy), as changing their id may change the id in the databse. It may
be necessary to copy them before renaming::

	new_objs = [copy.deepcopy(x) for x in old_objs]

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

__all__ = [
	'get_simple_uid',
]


### CONSTANTS & DEFINES ###

_CURR_UID = 0


### IMPLEMENTATION ###

def get_simple_uid (base='uid_%s'):
	"""
	Generate a unique id (UID).
	
	:Parameters:
		base : string
			The basic form for the UIDs generated. It should contain a formatting
			instruction for insertion of another string (i.e. "%s").
			
	:Returns:
		A UID as a string.
		
	This is actually a mediocre UID, which will only be unique within a session
	and only if used sensibly. However, it is good enough for a lot of purposes.
	Libraries with stricter and better UID generators are available elsewhere.
	
	For example::
	
		>>> get_simple_uid()
		'uid_1'
		>>> get_simple_uid()
		'uid_2'
		>>> get_simple_uid ('foo%sbar')
		'foo3bar'
				
	"""
	global _CURR_UID
	_CURR_UID += 1
	return base % str (_CURR_UID)


class BaseRenamer (object):
	"""
	Provide alternative unique names and later backtranslate them.
	
	This class allows the generation of new (and supposedly safe and unique)
	names from an original set and later backtranslation. Note it is not
	usuable directly - subclasses must provide some of the necessary renaming
	functionality - but would be used something like this::
	
		renamer = ObjRenamer()
		obj_list = [obj_1, obj_2, obj_3]
		# rename objects
		for item in obj_list:
			item.name = renamer.translate (item.name)
		# ... use the renamed objects ...
		for item in obj_list:
			item.name = renamer.backtranslate (item.name)		
	
	Some caveats:
	
	* If two input names are the same, they will result in different output
		names. 
	* If renamed objects are persisted from a database, and the name is their
		primary key, Bad Thing could happen.
		
	"""
	# TODO: we could allow non-unique names (many-to-one) or lookup names
	# and return the same newname if it's already occurred
	# TODO: allow the setting of wrapper objects that extract and set names
	# from objects?
	# TODO: if we get multiple of the same name, it will foul up transdict
	# TODO: store and return objects?
	
	def __init__ (self):
		"""
		C'tor.
		
		Subclasses may need to initialise their renaming machinery in their own
		c'tor.
		"""
		#self.get_name_fn = get_name_fn or lambda x: x
		#self.set_name_fn = set_name_fn or lambda x: x
		self._transdict = {}
		self._backdict = {}
	
	def translate (self, name):
		"""
		Provide a new name instead of this one.
		
		Note that in the current implementation, seperate calls to this method
		with the same name will give different "new" names.
		"""
		new_name = self._rename (name)
		assert (new_name not in self._backdict), "name '%s' is not unique"
		self._backdict[new_name] = name
		self._transdict[name] = new_name
		return new_name
		
	def backtranslate (self, name):
		"""
		Given a name generated by this translator, return the original name.
		"""
		return self._backdict[name]
	
	def _rename (self, name):
		"""
		Provide an alternate name.
		
		:Parameters:
			name : string
				A name to be translated, mangled or substituted.
				
		:Returns:
			A new name.
		
		This is the internal workhorse function that should be overridden in
		subclasses to provide different naming schemes. Recording the mapping
		between 
		"""
		raise NotImplementedError ('must override method in subclass')
		
		
class StrNumRenamer (BaseRenamer):
	"""
	A renamer using a simple constant string and incrementing number scheme.
	
	This basically duplicates `get_simple_uid` with the additional of
	back-translation, generating new names like "uid_3" and "seq-4-data".
	
	"""
	def __init__ (self, fmt_str='uid_%s'):
		"""
		C'tor, allowing the setting of the output format.
		
		:Parameters:
			fmt_str : string
				The basic form of names generated. It should contain a formatting
				instruction for insertion of another string (i.e. "%s").		
		
		"""
		BaseRenamer.__init__ (self)
		self._fmt_str = fmt_str
		self._curr_id = 0
		
	def _rename (self, name):
		self._curr_id += 1
		return self._fmt_str % str (self._curr_id)
	
	
### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod ()


### MAIN ###

if __name__ == '__main__':
	main()


### END ######################################################################
