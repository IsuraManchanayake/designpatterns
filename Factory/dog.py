#!/usr/bin/env python

from animal import IAnimal

class Dog(IAnimal):
	"""Dog class."""

	def __init__(self):
		"""Dog constructor"""
		print "a dog born"

	def shout(self):
		"""Dog's implementation of IAnimal.shout()"""
		print "woof woof"
