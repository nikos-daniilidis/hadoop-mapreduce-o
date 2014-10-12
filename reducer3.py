#!/usr/bin/python

'''
Find the total number of sales and the total sales value from all the stores.
Each line in purchases.txt is:
date\ttime\tstore name\titem description\tcost\tmethod of payment
e.g. 
2012-01-01      09:00   San Jose        Men's Clothing  214.05  Amex

The mapper produced tab seperated key-value pairs of the form
item_type,purchase_value

As I read the data, all the sales for a particular item type will be presented,
then the key will change and I'll be dealing with the next item type. I just 
keep adding all values and also keep a counter for all the sales I'ce seen. When 
I've processsed everything, I write the two numbers to output.
'''

import sys

salesValue = 0
salesNumber = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisSale = data_mapped

	#oldKey = thisKey
	salesValue += float(thisSale)
	salesNumber += 1

print 'Total sales value: %.2f' % salesValue
print 'Total number of sales: %d' % salesNumber
