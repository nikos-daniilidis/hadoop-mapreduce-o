#!/usr/bin/python

import sys, csv, string

def mapper():
	'''
	mapper_toptags.py, reducer_toptags.py
	Use the user forum data to find the top 10 tags ordered by the number of questions submitted under a tag. 
	IMHO, this is an example of a Top N problem which should not be solved using the approach given in Lesson 4 
	and in the "MapReduce Design Patterns" book. Here is why:
	1.	In the mapper stage, we do not have a global picture of how many questions a tag will appear in, even within the 
	 	portion of the data split which the mapper handles (unless we store the values for all 64 MB, sort them, and select 
		the top N).
	2.	The top N from an individual mapper is meaningless on the global scale, because we have no control over how the data
		is split to the mappers. The reducer will have to go through great pains to combine the top N from different mappers, 
		and will completely miss a popular tag which has been split across too many mappers.

	Input:
	======
	Read forum_node.tsv. The format of each line from forum_node.tsv is
	id title tagnames author_id body node_type parent_id abs_parent_id added_at score state_string last_edited_id last_activity_by_id...
	last_actitvity_at active_revision_id extra extra_ref_id extra_count marked 
	We need to extract the post tag, type of post (question, answer, comment), and the score of the post (this is not for the main quiz question but for further processing).

	Output:
	=======
	For each entry in forum_node.tsv, output a line of the form: 
	tag\ttype\tscore
	There might be several tags per post, print one line per tag (a tag is a word in the "tagnames" field)
	'''

	reader = csv.reader(sys.stdin, delimiter='\t') 	# read line by line, split input at \t characters
	splitTags = True

	for line in reader:
		if line[0] == "id":	# first line is just title
			continue
		elif len(line) == 19:
			# get the post id, type, and length
			if splitTags:
				post_tags_list = line[2].split(" ") # I am assuming here that the tag field is a space separated list of tags
			else:
				post_tags_list = [line[2]]			
			post_type = line[5]
			post_score = line[9]
			# print the output
			for post_tag in post_tags_list:
				print "{0}\t{1}\t{2}".format(post_tag, post_type, post_score)
		else:	# something went wrong, skip badly formatted data
			continue

if __name__=="__main__":
	mapper()

