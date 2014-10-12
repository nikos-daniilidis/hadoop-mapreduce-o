#!/usr/bin/python

import sys, string

def reducer():
	'''
	mapper_length.py, reducer_length.py 
	Work on data from the udacity forum (similar to Stack Exchange format). 
	Use the user post data to find the length of each question and the average length of the answers to that question.
	The dataset for this mapper was generated by exporting data from a SQL database.

	Input:
	======
	The feed from the mapper is:
	id\ttype\tlength
	and it comes sorted, which means I get all the answers for a  particular id, then I get the question for that id.
	The comments have been rejected by the mapper, so I don't see them

	Output:
	=======
	For each entry in forum_node.tsv, output a line of the form: 
	id\tquestion_length\taverage_answer_length
	'''
	oldId = None
	thisId = None
	thisType = None
	thisLength = 0
	lengthTotal = 0
	numTotal = 0
	lengthQuestion = 0

	for line in sys.stdin:
		data_mapped = line.strip().split("\t")
		if len(data_mapped) != 3:
			# Something has gone wrong. Skip this line.
			continue

		thisId, thisType, thisLength = data_mapped	# get the new entry	    

		if oldId and oldId != thisId:		# if there is a new user, print the results for the previous user
			if numTotal>0:
				print "{0}\t{1}\t{2}".format(oldId, lengthQuestion,float(lengthTotal)/numTotal)
			else:
				print "{0}\t{1}\t{2}".format(oldId, lengthQuestion,0)
			# don't forget to reset the counters
			lengthTotal = 0
			numTotal = 0
			lengthQuestion = 0

		# update the user, total length, counts 
		oldId = thisId
		if thisType=="answer":
			lengthTotal += int(thisLength)
			numTotal += 1
		elif thisType=="question":
			lengthQuestion = int(thisLength)
		else:
			# something is wrong
			print "Reducer warning: wrong node type fed from mapper."
			continue

	if oldId != None:# finally, print the last entry
		if numTotal>0:
			print "{0}\t{1}\t{2}".format(oldId, lengthQuestion,float(lengthTotal)/numTotal)
		else:
			print "{0}\t{1}\t{2}".format(oldId, lengthQuestion,0)

if __name__=="__main__":
	reducer()
