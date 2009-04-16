#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the relais.dev.renamer module, using nose.
"""

### IMPORTS ###

from relais.dev import renamer


### CONSTANTS & DEFINES ###

### TESTS ###

def test_get_simple_uid():
	"""
	Test the simplest case of logging.
	"""
	assert (renamer.get_simple_uid() == 'uid_1')
	assert (renamer.get_simple_uid() == 'uid_2')
	assert (renamer.get_simple_uid ('test%stest') == 'test3test')
	
class test_strnumrenamer (object):
	def test_ctor (self):
		a = renamer.StrNumRenamer()
		b = renamer.StrNumRenamer ('foo%s')
		c = renamer.StrNumRenamer ('foo%sbar')
		
	def test_renaming (self):
		orig_names = [str(x) for x in range(10)]
		rnmr = renamer.StrNumRenamer()
		new_names = []
		for o in orig_names:
			new_name = rnmr.translate (o)
			assert (new_name not in new_names)
			new_names.append (new_name)
		for idx, name in enumerate (new_names):
			print "new_names", new_names
			print "idx, name", idx, name
			print "backdict", rnmr._backdict
			old_name = rnmr.backtranslate (name)
			print "old_name", old_name
			assert (old_name == orig_names[idx])


### END ########################################################################
