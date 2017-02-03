#!/usr/bin/env python

from vehicle import Vehicle

class ThreeWheel(Vehicle):

	"""Three wheel type vehicle objects

	Attributes:
		_name: name of the three wheel
		_wheel_count: wheel count of the three wheel
	"""

	def __init__(self):
		"""Constructor for three wheel objects"""
		print "a three wheel created"
		self._name = "three wheel"
		self._wheel_count = 4

	def noise(self):
		"""Return the noise of the three wheel"""
		return "tuk tuk"