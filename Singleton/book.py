#!/usr/bin/env python

from threading import RLock

class Book(object):

	"""Reusable Book class using singleton design pattern
	
	Attributes:
		__instance: static singleton instance
		__lock : lock for the thread safety 
		name: book name
		author: book author
	"""

	__instance = None
	__lock = RLock()

	def __new__(cls):
		"""Return the Overridden __new__ of the object class.
		Uses the same __instance if available and else create a one.

		Returns:
			Singleton object
		"""
		with Book.__lock:
			if cls.__instance is None:
				cls.__instance = object.__new__(cls)
				cls.__instance.name = "Tarzan of the Apes"
				cls.__instance.author = "Edgar Rice Burroughs"
				print "new book has been created"
			else:
				print "using the same book"
			return cls.__instance

	def __init__(self):
		print "singleton object is ready"
