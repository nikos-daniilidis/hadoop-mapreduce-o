#!/usr/bin/python
'''
Find the mean amount of purchases for eacch day of the week, using 
a file with records of purchases. Make sure the program will run when using 
combiners. Each line in purchases.txt is:
date\ttime\tstore name\titem description\tcost\tmethod of payment
e.g. 
2012-01-01      09:00   San Jose        Men's Clothing  214.05  Amex

This means I need to pass the day of the week and purchase value to the 
reducer. I need to write them out to standard output, separated by a tab
key,value = day_of_week,purchase_value
'''
import sys, csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
daydict = {'0':'0_Monday',
	'1':'1_Tuesday',
	'2':'2_Wednesday',
	'3':'3_Thursday',
	'4':'4_Friday',
	'5':'5_Saturday',
	'6':'6_Sunday'}

for line in reader:
	if len(line) == 6:
		date = line[0]
		price = line[4]
		weekday = datetime.strptime(date, "%Y-%m-%d").weekday()  
		print "{0}\t{1}".format(daydict[str(weekday)], price)
    else:
		print 'Warning: Badly formatted  input line.\n'

