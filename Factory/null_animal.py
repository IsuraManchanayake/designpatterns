#!/usr/bin/env python

from animal import IAnimal

class NullAnimal(IAnimal):
	"""Null object class for IAnimal class.
	
	Has implemented __init__() and shout() methods to 
	encounter null reference errors.
	"""

	@classmethod
	def __init__(self):
		"""NullAnimal constructor"""
		print "an invisible animal born"

	@classmethod
	def shout(self):
		"""NullAnimal's implementation of IAnimal.shout()"""
		print "bleh-bleh-bleh"
