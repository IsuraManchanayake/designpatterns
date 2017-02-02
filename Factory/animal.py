#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class IAnimal:
	"""Abstract base class for animal."""

	__metaclass__ = ABCMeta

	@abstractmethod
	def shout(self):
		"""Abstract shout method"""
		pass

