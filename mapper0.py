#!/usr/bin/python

'''
Find the total sales per store using a file with records of purchases.
Each line in purchases.txt is:
date\ttime\tstore name\titem description\tcost\tmethod of payment
e.g. 
2012-01-01      09:00   San Jose        Men's Clothing  214.05  Amex

This means wwe need to pass the store names and purchase values to the 
reducer. We need to write them out to standard output, separated by a tab
'''

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		print "{0}\t{1}".format(store, cost)

