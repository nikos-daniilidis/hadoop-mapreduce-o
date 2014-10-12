#!/usr/bin/python

'''
Find the value of the highest individual sale for each separate store, 
using a file with records of purchases. Each line in purchases.txt is:
date\ttime\tstore name\titem description\tcost\tmethod of payment
e.g. 
2012-01-01      09:00   San Jose        Men's Clothing  214.05  Amex

This means we need to pass the store name and purchase value to the 
reducer. We need to write them out to standard output, separated by a tab
key,value = store_name,purchase_value
'''

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		print "{0}\t{1}".format(store, cost)

