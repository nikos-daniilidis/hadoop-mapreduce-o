#!/usr/bin/python

'''
Find the number of hits from the IP 10.99.99.186, using the server log file. 
The logfile is in Common Log Format:
IP id usrname [date time] "GET /path/to/page HTTP/1.1" 200 10469
e.g.
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

The mapper produced tab seperated key-value pairs of the form
IP, status

As I read the data, all the requests for a particular IP will be presented,
then the key will change and we'll be dealing with the next page. I just 
keep a counter for the hits from the current IP. When the key (IP) changes, 
I write the old IP and number of hits to output.
'''

import sys

numHits = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisStatus = data_mapped

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", numHits
		oldKey = thisKey;
		numHits = 0

	oldKey = thisKey
	numHits += 1

if oldKey != None:
	print oldKey, "\t", numHits

