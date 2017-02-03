#!/usr/bin/env python

from vehicle import Vehicle

class Bus(Vehicle):

	"""Bus type vehicle objects

	Attributes:
		_name: name of the vehicle
		_wheel_count: wheel count of the vehicle
	"""

	def __init__(self):
		"""Constructor for bus objects"""
		print "a bus created"
		self._name = "bus"
		self._wheel_count = 4

	def noise(self):
		"""Return the noise of the bus"""
		return "broom broom"