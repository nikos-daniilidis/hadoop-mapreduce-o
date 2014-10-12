#!/usr/bin/python

'''
Find the most popular file on the website, and the number of times it appears in the log.
The logfile is in Common Log Format:
IP id usrname [date time] "GET /path/to/page HTTP/1.1" 200 10469
e.g.
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

The mapper produced tab seperated key-value pairs of the form
filename, page

As I read the data, all the requests for a particular page will be presented,
then the key will change and we'll be dealing with the next page. I just 
keep a counter for the hits to the current page. I also keep the most popular 
filename and number of hits, and update them whenever I see a file with more hits. 
In the end I print the filename and number of hits with the max values.
'''

import sys

currentHits = 0
maxHits = 0
oldKey = None
mostPopular = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisStatus = data_mapped

	if oldKey and oldKey != thisKey:
		#print oldKey, "\t", numHits
		if currentHits > maxHits:
		maxHits = currentHits
		mostPopular = oldKey
		oldKey = thisKey;
		currentHits = 0

	oldKey = thisKey
	currentHits += 1


if currentHits > maxHits:
	maxHits = currentHits
	mostPopular = thisKey

if oldKey != None:
	print mostPopular, "\t", maxHits

