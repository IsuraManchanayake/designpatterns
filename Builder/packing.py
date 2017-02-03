#!/usr/bin/env python

from abc import ABCMeta

class Packing(object):

	"""Abstract base class for the packing of an Item object

	Attributes:
		_name: str - name of the packing
	"""

	__metaclass__ = ABCMeta

	def name(self):
		"""Returns the name of the packing"""
		return self._name
