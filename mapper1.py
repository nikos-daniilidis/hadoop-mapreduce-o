#!/usr/bin/python

'''
Find the total sales per item type using a file with records of purchases.
Each line in purchases.txt is:
date\ttime\tstore name\titem description\tcost\tmethod of payment
e.g. 
2012-01-01      09:00   San Jose        Men's Clothing  214.05  Amex

This means I need to pass the item type and purchase value to the 
reducer. I need to write them out to standard output, separated by a tab
key,value = item_type,purchase_value
'''

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		print "{0}\t{1}".format(item, cost)

