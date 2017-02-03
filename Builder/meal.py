#!/usr/bin/env python

class Meal(object):
	"""Meal consisting several Item objects

	Attributes:
		__items : list - list of Item objects
	"""

	def __init__(self, items = []):
		"""Constructor of the Meal object
		
		Args:
			items: optional parameter of list type
		"""
		if not items and type(items) == list:
			self.__items = items
		else:
			self.__items = []

	def add_item(self, item):
		"""Add item to list of items
		
		Args:
			item: Item - item to be appended
		"""
		self.__items.append(item)

	def get_cost(self):
		"""Get total price of all the items
		
		Returns:
			total price
		"""
		return sum([item.price() for item in self.__items])

	def show_items(self):
		"""Print all the items of the meal"""
		print "This is a meal talking"
		print "I have", len(self.__items), "item(s) in my meal"
		if self.__items:
			print "They are:"
			for item in self.__items:
				print "name =", item.name(),
				print ": packing =", item.packing().name(),
				print ": price =", item.price()
