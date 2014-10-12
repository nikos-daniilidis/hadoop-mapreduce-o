#!/usr/bin/python

import sys, csv, string

def mapper():
	'''
	mapper_length.py, reducer_length.py 
	Use the user post data to find the length of each question and the average length of the answers to that question.
	Work on data from the udacity forum (similar to Stack Exchange format). The dataset for this mapper was generated 
	by exporting data from a SQL database.

	Input:
	======
	Read forum_node.tsv. The format of each line from forum_node.tsv is
	id title tagnames author_id body node_type parent_id abs_parent_id added_at score state_string last_edited_id last_activity_by_id...
	last_actitvity_at active_revision_id extra extra_ref_id extra_count marked 
	We need to extract the post id, type of post (question, answer, comment), and the length of the body (in characters).

	Output:
	=======
	For each entry in forum_node.tsv, output a line of the form: 
	id\ttype\tlength
	'''

	reader = csv.reader(sys.stdin, delimiter='\t') 	# read line by line, split input at \t characters

	for line in reader:
		if line[0] == "id":	# first line is just title
			continue
		elif len(line) == 19:
			# get the post id, type, and length
			post_type = line[5]
			post_length = len(line[4])
			if post_type == "question": # for questions, the id is under the "id" column
				post_id = line[0]
			elif post_type == "answer": # for answers, the id is in the "abs_parent_id" column
				post_id = line[7]

			if post_type != "comment":	# print for processing by the reducer, if it is not a comment
				print "{0}\t{1}\t{2}".format(post_id, post_type, post_length)
		else:	# something went wrong, skip badly formatted data
			continue

if __name__=="__main__":
	mapper()

