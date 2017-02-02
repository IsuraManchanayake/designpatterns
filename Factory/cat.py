#!/usr/bin/env python

from animal import IAnimal

class Cat(IAnimal):
	"""Cat class."""

	def __init__(self):
		"""Cat constructor"""
		print "a cat born"

	def shout(self):
		"""Cat's implementation of IAnimal.shout()"""
		print "meow meow"
