#!/usr/bin/python
'''
Find the sum of purchases for each day of the week, using 
a file with records of purchases. The reducer code is written in 
such a way that it can be used to produce intermediate values at 
the mappers. Each line in purchases.txt is:
date\ttime\tstore name\titem description\tcost\tmethod of payment
e.g. 
2012-01-01      09:00   San Jose        Men's Clothing  214.05  Amex

The mapper output was key, value pairs as:
key,value = day_of_week,purchase_value
The reducer will keep a list off all prices for each day of the week, 
and add to the list as new purchases are processed. When the day changes, 
the reducer prints out the day of the week and the sum of the sales for that 
day. 
'''
import sys, string
import math

oldKey = None
priceList = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisPrice = data_mapped

	if oldKey and oldKey != thisKey:
		meanPrice = math.fsum(priceList)#/len(priceList)
		print "{0}\t{1}".format(oldKey,meanPrice)
		oldKey = thisKey; # reduntant but whatever
		priceList = []

	oldKey = thisKey
	priceList.append(float(thisPrice))

if oldKey != None:
	meanPrice = math.fsum(priceList)#/len(priceList)
	print "{0}\t{1}".format(oldKey,meanPrice)

