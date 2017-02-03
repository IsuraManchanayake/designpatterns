#!/usr/bin/env python

from meal_builder import MealBuilder

def main():
	meal_builder = MealBuilder()

	vmeal = meal_builder.prepare_veg_meal()
	nvmeal = meal_builder.prepare_non_veg_meal()

	vmeal.show_items()
	nvmeal.show_items()

	print "price of the veg-meal :", vmeal.get_cost()
	print "price of the non-veg-meal :", nvmeal.get_cost()


if __name__ == '__main__':
	main()