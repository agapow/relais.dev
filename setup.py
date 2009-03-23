#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A setup script using setuptools.
"""


### IMPORTS ###

from setuptools import setup, find_packages
import os

from relais.dev import __version__


### SETUP ###

setup (
	name='relais.dev',
	version=__version__,
	description="Development utilities and functions for Relais",
	long_description=open("README.txt").read() + "\n" +
		open(os.path.join("docs", "HISTORY.txt")).read(),
	# Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Scientific',
	],
	keywords='',
	author='Paul-Michael Agapow',
	author_email='agapow@bbsrc.ac.uk',
	url='http://www.agapow.net/software/relais.dev',
	license='BSD',
	packages=find_packages(exclude=[
		"*.test",
		"*.test.*",
		"test.*",
		"test",
		'ez_setup',
	]),
	test_suite = 'nose.collector',
	namespace_packages=['relais'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'setuptools',
		# -*- Extra requirements: -*-
	],
	entry_points="""
		# -*- Entry points: -*-
	""",
	)


### END ###
