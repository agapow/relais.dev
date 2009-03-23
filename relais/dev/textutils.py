#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various utilities for manipulating text and strings.
"""

### IMPORTS ###

import re, time, StringIO, htmlentitydefs
from os import linesep


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###


##
# Removes HTML or XML character references and entities from a text string.
#
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.

def unescape (text):
	"""
	Convert HTML/XML character references and entities to simple characters.
	
	:Parameters:
		text : string
			A string containing character entities, e.g. "foo &amp; bar"
			
	:Returns:
		A sanitized string.
	
	Stolen from Frederick Lundh <http://effbot.org/zone/re-sub.htm>.
	"""
	def fixup (m):
		text = m.group (0)
		if text[:2] == "&#":
			# character reference
			try:
				if text[:3] == "&#x":
					return unichr (int (text[3:-1], 16))
				else:
					return unichr (int (text[2:-1]))
			except ValueError:
				pass
		else:
			# named entity
			try:
				text = unichr (htmlentitydefs.name2codepoint[text[1:-1]])
			except KeyError:
				pass
		return text # leave as is
	return re.sub ("&#?\w+;", fixup, text)


def is_int_str (int_str):
	"""
	Is this the string representation of an integer?

	Used in tests and prior to conversion functions.
	"""
	try:
		x = int (int_str)
		return True
	except:
		return False


def is_float_str (float_str):
	"""
	Is this the string representation of an float?

	Used in tests and prior to conversion functions.
	"""
	try:
		x = float (float_str)
		return True
	except:
		return False


def delete_str_posns (in_str, posn_list):
	"""
	Gven a string and a list of positions, delete those positions.

	Note that the list is assumed to be sorted.
	"""
	#theOutStrm = StringIO()
	#theOutStrm.write (in_str[:posn_list[0]])
	#for i in xrange (len(posn_list)-1):
	#	theOutStrm.write (in_str[posn_list[i]+1:posn_list[i+1]])
	#theOutStrm.write (in_str[posn_list[-1]+1:])
	#theOutStrm.seek(0)
	#return theOutStrm.read()
	theOutStrm = StringIO()
	if (type(posn_list[0]) == type(1)):
		theStart = posn_list[0]
	elif (type(posn_list[0]) == type([])):
		theStart = posn_list[0][0]
	theOutStrm.write (in_str[:theStart])
	for i in xrange (len(posn_list)-1):
		if (type(posn_list[i]) == type(1)):
			theStart = posn_list[i]
		elif (type(posn_list[i]) == type([])):
			theStart = posn_list[i][1]
		if (type(posn_list[i+1]) == type(1)):
			theStop = posn_list[i+1]
		elif (type(posn_list[i+1]) == type([])):
			theStop = posn_list[i+1][0]
		theOutStrm.write (in_str[theStart+1:theStop])
	if (type(posn_list[-1]) == type(1)):
		theStart = posn_list[-1]
	elif (type(posn_list[-1]) == type([])):
		theStart = posn_list[-1][1]
	theOutStrm.write (in_str[theStart+1:])
	theOutStrm.seek(0)
	return theOutStrm.read()


def ends_with_patt (in_str, end_pattern):
	"""
	Does this string end with this pattern?

	"""
	return re.search ("%s$" % end_pattern, in_str)



def getCurrTimeStr ():
	"""
	Return the current time formatted as '2005-01-25 17:32'.
	"""
	return time.strftime ("%Y-%m-%d %H:%M", time.localtime())


def find_not (str, c):
	"""
	Find the first index in a string that is not c.
	"""
	for i in range (len (str)):
		if (str[i] != c):
			return i
	return -1


def rfind_not (str, c):
	"""
	Find the last index in a string that is not c.
	"""
	for i in range (len(str) -1, -1, -1):
		if (str[i] != c):
			return i
	return -1


def canonical_eoln (str):
	"""
	Convert all strings to a canonical form with unix end-of-lines.
	"""
	theRetStr = str.replace ('\r\n', '\n') # DOS -> Unix
	theRetStr = theRetStr.replace ('\r', '\n') # Classic Mac -> Unix
	return theRetStr


def native_eoln (str):
	"""
	Convert all strings to a native form as regards end-of-lines.
	"""
	theRetStr = str.replace ('\r\n', linesep)			 # DOS -> native
	if (linesep != '\r'):
		theRetStr = theRetStr.replace ('\r', linesep)	# Classic Mac -> native
	if (linesep != '\n'):
		theRetStr = theRetStr.replace ('\r', linesep)	# Unix -> native
	return theRetStr

