#!/usr/bin/python

import sys, string

def reducer():
	'''
	mapper_time.py, reducer_time.py
	Use the user post data to determine at what time of the day each student has the largest number of posts. 

	Input:
	======
	The format of each line from the reducer is: 
	user_id\thour
	These come after shuffle/sort, so the users are sorted, and the times are also sorted. 
	This allows counting the amount of hits for each posting time, for each user, by keeping 
	track of the thisUser, oldUser, thisHour oldHour values.

	Output:
	=======
	For each user, output the hour at which they posted the most:
	user_id\thour 
	'''
	oldUser = None
	thisUser = None
	oldHour = None
	thisHour = None
	maxHourList = []
	currentCounts = 0
	maxCounts = 0

	for line in sys.stdin:
		data_mapped = line.strip().split("\t")
		if len(data_mapped) != 2:
			continue        # Something has gone wrong. Skip this line.

		thisUser, thisHour = data_mapped	# get the new entry	    

		if oldUser and oldUser != thisUser:		# if there is a new user, print the results for previous user
			for Hour in maxHourList:			# the results for top hours are in a list, print all the elements on different lines
				print "{0}\t{1}".format(oldUser,str(int(Hour)))
			maxCounts = 0		# also remember to reset the counters and record-keeper
			currentCounts = 0
			maxHourList = []
		elif oldHour and oldHour != thisHour:		# if this is the same user and a new hour, just reset the counts for the hour
			currentCounts = 0
		else: 
			pass
	   
		oldUser = thisUser	# update the user, hour, and counts 
		oldHour = thisHour
		currentCounts += 1

		if currentCounts == maxCounts:		# if there is a tie, I need to store all the values which have equal counts
			maxHourList.append(thisHour)
		elif currentCounts > maxCounts:		# if there is no tie, just place a single item in the maxHourList
			maxHourList = [thisHour]
			maxCounts = currentCounts

	if oldUser != None:# finally, print the last entry
		for Hour in maxHourList:		# the results for top hours are in a list, print all the elements on different lines
			print "{0}\t{1}".format(oldUser,str(int(Hour)))

if __name__=="__main__":
	reducer()
