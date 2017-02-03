#!/usr/bin/env python

from packing import Packing

class Wrapper(Packing):

	"""Wrapper object

	Attributes:
		_name: str - name of the packing
	"""

	def __init__(self):
		"""Constructor for the Wrapper object"""
		self._name = "Wrapper"
