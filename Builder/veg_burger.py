#!/usr/bin/env python

from burger import Burger

class VegBurger(Burger):

	"""Vegitable Burger type

	Attributes:
		_name: str - name of the item
		_packing: Packing - packing of the item
		_price: float - price of the item
	"""

	def __init__(self):
		"""Constructor for VegBurger"""
		super(VegBurger, self).__init__()
		self._name = "VegBurger"
		self._price = 150.00