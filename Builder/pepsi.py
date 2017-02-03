#!/usr/bin/env python

from cold_drink import ColdDrink

class Pepsi(ColdDrink):

	"""Pepsi, type of cold drink

	Attributes:
		_name: str - name of the item
		_packing: Packing - packing of the item
		_price: float - price of the item
	"""

	def __init__(self):
		"""Constructor for the Pepsi"""
		super(Pepsi, self).__init__()
		self._name = "Pepsi"
		self._price = 50.00
