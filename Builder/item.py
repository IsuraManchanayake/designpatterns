#!/usr/bin/env python

from abc import ABCMeta

class Item(object):

	"""Abstract base class for all item types.

	Attributes:
		_name: str - name of the item
		_packing: Packing - packing of the item
		_price: float - price of the item
	"""

	__metaclass__ = ABCMeta

	def name(self):
		"""Return name of the item."""
		return self._name

	def packing(self):
		"""Return packing of the item."""
		return self._packing

	def price(self):
		"""Return price of the item."""
		return self._price
