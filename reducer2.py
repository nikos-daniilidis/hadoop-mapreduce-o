#!/usr/bin/python

import sys

maxSale = -1.
oldKey = None

'''
Find the value of the highest individual sale for each separate store, 
using a file with records of purchases. Each line in purchases.txt is:
date\ttime\tstore name\titem description\tcost\tmethod of payment
e.g. 
2012-01-01      09:00   San Jose        Men's Clothing  214.05  Amex
The mapper produced tab seperated key-value pairs of the form
store_name,purchase_value

As I read the data, all the sales for a particular store will be presented,
then the key will change and we'll be dealing with the next store. As I read, 
I keepa value for the current store maximum sale. When the store name
changes, write the maximum value for the previous store to the output.
'''

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisSale = data_mapped

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", maxSale
		oldKey = thisKey
		maxSale = -1.

	oldKey = thisKey
	if float(thisSale)>maxSale:
	maxSale = float(thisSale)

if oldKey != None:
	print oldKey, "\t", maxSale

