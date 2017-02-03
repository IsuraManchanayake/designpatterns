#!/usr/bin/env python

from meal import Meal
from veg_burger import VegBurger
from chicken_burger import ChickenBurger
from pepsi import Pepsi
from coke import Coke

class MealBuilder(object):

	"""Meal builder class implementing the builder design pattern"""

	def prepare_veg_meal(self):
		"""Make vegetarian meal builder method

		Returns:
			vegetarian meal
		"""
		vmeal = Meal()
		vmeal.add_item(VegBurger())
		vmeal.add_item(Pepsi())

		print "vegetarian meal created"

		return vmeal

	def prepare_non_veg_meal(self):
		"""Make non-vegetarian meal builder

		Returns:
			non-vegetarian meal 
		"""
		nvmeal = Meal()
		nvmeal.add_item(ChickenBurger())
		nvmeal.add_item(Coke())

		print "non-vegetarian meal created"

		return nvmeal
