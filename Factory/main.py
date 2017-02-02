#!/usr/bin/env python

from factory import AnimalFactory

f1 = AnimalFactory()
f2 = AnimalFactory()

duck1 = f1.get_animal("puk")
duck2 = f1.get_animal("duck")
dog1 = f2.get_animal("dog")
cat1 = f1.get_animal("cat")

duck1.shout()
dog1.shout()
cat1.shout()

print "number of f1 animals :", f1.get_object_count()
print "number of f2 animals :", f2.get_object_count()