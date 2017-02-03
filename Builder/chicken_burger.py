#!/usr/bin/env python

from burger import Burger

class ChickenBurger(Burger):

	"""Chicken Burger type

	Attributes:
		_name: str - name of the item
		_packing: Packing - packing of the item
		_price: float - price of the item
	"""

	def __init__(self):
		"""Constructor for ChickenBurger"""
		super(ChickenBurger, self).__init__()
		self._name = "ChickenBurger"
		self._price = 200.00
