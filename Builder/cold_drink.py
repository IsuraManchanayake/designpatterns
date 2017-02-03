#!/usr/bin/env python

from item import Item
from bottle import Bottle
from abc import ABCMeta

class ColdDrink(Item):

	"""Abstract base class for all cold drink types

	Attributes:
		_name: str - name of the item
		_packing: Packing - packing of the item
		_price: float - price of the item
	"""

	__metaclass__ = ABCMeta

	def __init__(self):
		"""Constructor for the ColdDrink type"""
		self._packing = Bottle()
