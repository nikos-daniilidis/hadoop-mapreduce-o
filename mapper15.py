#!/usr/bin/python

import sys, csv, string

def mapper():
	'''
	mapper_time.py, reducer_time.py
	Use the user post data to determine at what time of the day each student has the largest number of posts. 

	Input:
	======
	Use the user post data to determine at what time of the day each student has the largest number of posts
	Read forum_node.tsv. The format of each line from forum_node.tsv is:
	id title tagnames author_id body node_type parent_id abs_parent_id added_at ...
	score state_string last_edited_id last_activity_by_id last_actitvity_at active_revision_id ...
	extra extra_ref_id extra_count marked 

	The posting time is in the format YYYY-MM-DD HH:MM:SS.SSSSSS+00, and we need to extract the hour.

	Output:
	=======
	For each entry in forum_node.tsv, output a line of the form: 
	user_id\thour
	where hour is extracted from added_at
	'''
	# read line by line, split input at \t characters
	reader = csv.reader(sys.stdin, delimiter='\t')

	for line in reader:
		if line[0]=="id": # first line is just title
			continue
		elif len(line)==19:
			author_id = line[3]
			added_at = line[8]
			hour = added_at.split(":")[0].split(" ")[1]	
			print "{0}\t{1}".format(author_id, hour)
		else: # something went wrong, skip badly formatted data
			continue

if __name__=="__main__":
	mapper()

