#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various functions for working with the Python Imaging Library.
"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

from PIL import Image, ImageChops


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def crop_to_content (img, bg_clr, padding=None):
	"""
	Return an image that is the original cropped down to its content.
	
	:Paramters:
	
		img : PIL image
			The image to be cropped.
		
		bg_clr
			The background colour of the original image, which is necessary to
			detect content.
		
		padding
			How much space to leave around the content. By default it is 0.
	
	From Frederik Lundh's example on python-list, October 2003.
	"""
	## Preconditions
	if (padding is not None): assert (0 <= padding)
	## Main:
	if (img.mode != 'RGB'):
		img = img.convert ('RGB')
	wt, ht = img.size
	mask = Image.new ('RGB', img.size, bg_clr)
	diff = ImageChops.difference (img, mask)
	bbox = diff.getbbox()
	if bbox:
		if (padding):
			bbox = (
				max (0, bbox[0]-padding),
				max (0, bbox[1]-padding),
				min (bbox[2]+padding, wt),
				min (bbox[3]+padding, ht),
			)
		return img.crop (bbox)
	else:
		return None



### TEST & DEBUG ###

def _doctest ():
	import doctest
	doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
	_doctest()

	
### END ###################################################################
