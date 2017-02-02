#!/usr/bin/env python

from duck import Duck
from dog import Dog
from cat import Cat
from null_animal import NullAnimal

class AnimalFactory(object):
	"""Factory class of Animal objects.

	AnimalFactory object keeps track of all animals it 
	produced.

	Attributes:
		__factory_objects(private): number of animals that the factory object has initialised.
	"""

	def __init__(self):
		"""Constructor of the AnimalFactory class."""
		self.__factory_objects = 0

	def get_animal(self, animal_type):
		"""Factory method for the Animal objects.
	
		Args:
			animal_type: instance of a str to identify
				the type.

		Returns:
			Initialised animal object.
		"""
		if animal_type is not None and type(animal_type) == str:
			animal_type = animal_type.lower()

		if animal_type is None:
			return NullAnimal()
		elif animal_type == "duck":
			self.__factory_objects += 1
			return Duck()
		elif animal_type == "dog":
			self.__factory_objects += 1
			return Dog()
		elif animal_type == "cat":
			self.__factory_objects += 1
			return Cat()
		else:
			return NullAnimal()

	def get_object_count(self):
		"""get method for the __factory_objects.
		
		Returns:
			__factory_objects
		"""
		return self.__factory_objects
