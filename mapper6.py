#!/usr/bin/python

'''
Find the most popular file on the website, and the number of times it appears in the log.
The logfile is in Common Log Format:
IP id usrname [date time] "GET /path/to/page HTTP/1.1" 200 10469
e.g.
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

Use the filename as key, and choose some value to pass to the reducer. I need to 
write them out to standard output, separated by a tab
key,value = filename, page
'''

import sys
from urlparse import urlparse

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		ip, usrid, usrname, time, zone, reqtype, page, protocol, status, size = data
	#print page
	if len(page)>1:
		if '.php?' not in page:
			data = page.split('/')
			filename = data[-1]
		else:
			data = page.strip('/').split('.php?')
			filename = data[0]+'.php'     
		print "{0}\t{1}".format(filename, page)

