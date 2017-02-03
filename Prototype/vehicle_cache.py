#!/usr/bin/env python

from car import Car
from bus import Bus
from three_wheel import ThreeWheel

class VehicleCache(object):
	
	"""Cache class for the vehicle types

	_vehicle_dict keeps track of the 3 types of vehicles mentioned here. For
	requesting type of vehicles, new vehicle is created by deep copying the
	existing vehicle caches of _vechicle_dict. get_vehicle() returns None 
	unless load_cache() is not called before.

	Attributes:
		_vehicle_dict: cache dictionary of vehicles (str => Vehicle)
	"""

	_vehicle_dict = {}

	@classmethod
	def load_cache(cls):
		"""Load cache objects before get_vehicle() method"""
		car = Car()
		cls._vehicle_dict["car"] = car

		bus = Bus()
		cls._vehicle_dict["bus"] = bus

		three_wheel = ThreeWheel()
		cls._vehicle_dict["three wheel"] = three_wheel

	@classmethod
	def get_vehicle(cls, vehicle_type = None):
		"""Get vehicle for given typename of the vehicle"""
		try:
			if not vehicle_type:
				return None
			else:
				return cls._vehicle_dict[vehicle_type]
		except KeyError:
			return None
