#!/usr/bin/python

import sys, string

def reducer():
	'''
	mapper_toptags.py, reducer_toptags.py
	Use the user forum data to find the top 10 tags ordered by the number of questions submitted under a tag. 

	Input:
	======
	The input being fed from the mapper after shuffle/sort is: 
	tag\ttype\tscore
	Since the results are sorted, we can analyze separately all the questions for each tag, all the answers for each tag, etc.

	Output:
	=======
	The output is a list of 10 items, of the form:
	tag\tcounts
	'''
	oldTag = None
	oldType = None
	foundQuestion = False
	thisTag = None
	currentCounts = 0
	topTen = [] # the topTen list will hold up to ten tuples (tag,counts) of the top ten tags and the counts they receive

	for line in sys.stdin:
		data_mapped = line.strip().split("\t")
		if len(data_mapped) != 3: # Something has gone wrong. Skip this line.
			continue

		# get the new entry
		thisTag, thisType, thisScore = data_mapped	
		#if thisTag=="discussion":
		#	print currentCounts	    

		if oldTag and oldTag != thisTag:		# if there is a new tag, place the results for the previous tag in the topTen list
			if foundQuestion:		# if there is a new tag and we were processing a question, place the results for the previous tag in the topTen list
				foundQuestion = False
				inserted = False
				for i,ln in enumerate(topTen):
					if currentCounts>ln[1]:
						topTen.insert(i,(oldTag,currentCounts))
						inserted = True
						break
				if not inserted and len(topTen)<10:
					topTen.insert(len(topTen)+1,(oldTag,currentCounts))
				if len(topTen)>10:
					topTen.pop()
			# do not forget to reset the counter
			currentCounts = 0		

		# update the tag and counts 
		oldTag = thisTag
		oldType = thisType
		if thisType=="question":
			currentCounts += 1
			foundQuestion = True

	if oldTag != None:	# place the last entry into the list, if it belongs there
		inserted = False
		for i,ln in enumerate(topTen):
			if currentCounts>ln[1]:
				topTen.insert(i,(oldTag,currentCounts))
				inserted = True
				break
		if not inserted and len(topTen)<10:
			topTen.insert(len(topTen)+1,(oldTag,currentCounts))
		if len(topTen)>10:
			topTen.pop()

	# and print the output
	for ln in topTen:
		print "{0}\t{1}".format(ln[0],ln[1])

if __name__=="__main__":
	reducer()
