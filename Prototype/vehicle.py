#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Vehicle(object):

	"""Abstract base class for all vehicle objects

	Attributes:
		_name: str - name of the vehicle
		_wheel_count: int - wheel count of the vehicle		
	"""

	__metaclass__ = ABCMeta

	def name(self):
		"""Return name of the vehicle"""
		return self._name

	def wheel_count(self):
		""""Return wheel count of the vehicle"""
		return self._wheel_count

	def clone(self):
		"""Create a copy of the object"""
		return deepcopy(self)

	@abstractmethod
	def noise(self):
		"""Return the sound of the vehicle"""
		pass