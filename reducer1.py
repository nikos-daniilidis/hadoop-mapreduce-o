#!/usr/bin/python

'''
Find the total sales for each item type using a file with records of purchases.
Each line in purchases.txt is:
date\ttime\tstore name\titem description\tcost\tmethod of payment
e.g. 
2012-01-01      09:00   San Jose        Men's Clothing  214.05  Amex
The mapper produced tab seperated key-value pairs of the form
item_type,purchase_value

As I read the data, all the sales for a particular item type will be presented,
then the key will change and I'll be dealing with the next item type. I just 
keep adding all values for item type until it changes. When the item type 
changes, I write the data to the output.
'''

import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisSale = data_mapped

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", salesTotal
		oldKey = thisKey;
		salesTotal = 0

	oldKey = thisKey
	salesTotal += float(thisSale)

if oldKey != None:
	print oldKey, "\t", salesTotal

