#!/usr/bin/env python

from vehicle_cache import VehicleCache

def main():
	VehicleCache.load_cache()

	car1 = VehicleCache.get_vehicle("car")
	car2 = VehicleCache.get_vehicle("car")
	bus = VehicleCache.get_vehicle("bus")
	three_wheel = VehicleCache.get_vehicle("three wheel")

	if car1 is car2:	# True
		print "car1 and car2 are same"
	else:
		print "car1 and car2 are distinct objects but duplicates"

	for vehicle in [car1, car2, bus, three_wheel]:
		print vehicle.name(), "sounds", vehicle.noise()

if __name__ == '__main__':
	main()