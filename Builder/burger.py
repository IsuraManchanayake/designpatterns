#!/usr/bin/env python

from item import Item
from wrapper import Wrapper
from abc import ABCMeta

class Burger(Item):

	"""Abstract base class for all burger types

	Attributes:
		_name: str - name of the item
		_packing: Packing - packing of the item
		_price: float - price of the item
	"""

	__metaclass__ = ABCMeta

	def __init__(self):
		"""Constructor for Burger"""
		self._packing = Wrapper()
