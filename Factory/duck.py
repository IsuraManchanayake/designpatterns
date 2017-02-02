#!/usr/bin/env python

from animal import IAnimal

class Duck(IAnimal):
	"""Duck class."""

	def __init__(self):
		"""Duck constructor"""
		print "a duck born"

	def shout(self):
		"""Duck's implementation of IAnimal.shout()"""
		print "quack quack"
