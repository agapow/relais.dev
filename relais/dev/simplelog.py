#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic logging facilities.

These wrap the Python standard logging function to provide straightforward
and consistent logging functions, with sensible defaults for most ReLaIS
logging needs in single line calls.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

import logging


## CONSTANTS & DEFINES: ###

### IMPLEMENTATION ###

def make_logger (name=None, handler=None, filemode=None,
   msg_fmt=None, date_fmt=None, level=logging.DEBUG):
   """
   Return a basic logger.

   The default behaviour is to create a logger 'relais' that send every
   message to stderr, labelled with the date-time, name and level. This serves
   as the basis for all other loggers.

   :Parameters:
      name
         The title of the logger ('relais' by default).
      handler
         The destination of the messages. If not defined, it is set to stderr.
         If a string, this is interpreted as the path of a file to log to.
         Otherwise, it treated as a Handler object for the logger.
      filemode
         The filemode for the file handler created if the `handler` param is
         a file path.
      msg_fmt
         The format to use for displaying messages. Defaults to showing the
         date-time, name and level.
      date_fmt
         How to display the date, defaults to international format.
      level
         What messages to display. Displays to all.

   For example::

      >>> lgr = make_logger()
      >>> lgr.info ("what?")

   """
   # if no logger name is given, set it to current script
   if (name is None):
      name = 'relais'

   # if no handler given, set to stdout
   if (handler is None):
      handler = logging.StreamHandler()
   # else if handler is a string, assume it's a filepath
   elif (type (handler) == type ('')):
      if (filemode is None):
         filemode = 'w+'
      handler = logging.FileHandler (handler, filemode)
   # otherwise assume it's a handler

   # set up message format
   if (msg_fmt is None):
      msg_fmt = '%(asctime)s %(name)-8s %(levelname)s: %(message)s'
   if (date_fmt is None):
      date_fmt = '%Y-%m-%d %H:%M:%S'
   formatter = logging.Formatter (msg_fmt, date_fmt)
   handler.setFormatter (formatter)

   # create and init logger
   logger = logging.getLogger (name)
   logger.setLevel (level)
   logger.addHandler (handler)

   return logger


def make_debug_logger (*args, **kwargs):
   """
   Create a logger for debugging purposes.

   This makes a logger 'relais.debug', and displays messages without date
   or time and with the location of the debugging call.

   """
   # TODO: what if the caller set the filename?
   # TODO: what if the caller sets the name?
   msg_fmt = '%(module)s:%(funcName)s:%(lineno)d %(levelname)s: %(message)s'
   return make_logger (name='relais.debug', msg_fmt=msg_fmt)


def make_daemon_logger (*args, **kwargs):
   """
   Create a logger to be used by daemon processes.

   This makes a logger 'relais.daemon', and spools messages to a file. The
   filename is determined from the filename param, or set to 'relais.daemon'.

   """
   # TODO: what if the caller sets the name?
   filename = kwargs.get ('handler', None)
   if (filename is None):
      kwargs['handler'] = kwargs.get ('name', 'relais.daemon') + '.log'
   kwargs['name'] = 'relais.daemon'
   return make_logger (*args, **kwargs)


def get_logger (name='relais'):
	"""
	Get a pre-existing logger by name.
	
	A convenience function, that just provides a default name for the
	logger and avoids having to import logging for the single call.
	"""
	# TODO: what happens if logger doesn't exist?
	return logging.getLogger (name)
	

def named_log (msg, name='relais'):
	"""
	Another convenience function
	
	A convenience function, that just provides a default name for the
	logger and avoids having to import logging for the singel call.
	"""
	# TODO: what about defining level of message?
	# TODO: need a logger that can accept mutliple arguments
	logger = get_logger (name)
	logger.info (msg)



### TEST & DEBUG ###

def _doctest ():
   import doctest
   doctest.testmod (optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)


### MAIN ###

if __name__ == '__main__':
   _doctest()


### END ########################################################################
