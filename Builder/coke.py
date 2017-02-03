#!/usr/bin/env python

from cold_drink import ColdDrink

class Coke(ColdDrink):

	"""Coke, type of cold drink

	Attributes:
		_name: str - name of the item
		_packing: Packing - packing of the item
		_price: float - price of the item
	"""

	def __init__(self):
		"""Constructor for the Coke"""
		super(Coke, self).__init__()
		self._name = "Coke"
		self._price = 40.00
