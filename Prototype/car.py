#!/usr/bin/env python

from vehicle import Vehicle

class Car(Vehicle):

	"""Car type vehicle objects

	Attributes:
		_name: name of the vehicle
		_wheel_count: wheel count of the vehicle
	"""

	def __init__(self):
		"""Constructor for car objects"""
		print "a car created"
		self._name = "car"
		self._wheel_count = 4

	def noise(self):
		"""Return the noise of the car"""
		return "broom broom"