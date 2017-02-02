#!/usr/bin/env python

from book import Book

b1 = Book()
b2 = Book()

if b1 is b2:	# True
	print "both books are same"
else:
	print "books are not same"