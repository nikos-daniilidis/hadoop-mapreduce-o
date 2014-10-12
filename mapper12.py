#!/usr/bin/python

'''
Combine two data sets, based on posts from the udacity forum. Format of each line from forum_node.tsv:
id title tagnames author_id body node_type parent_id abs_parent_id added_at score state_string last_edited_id last_activity_by_id last_actitvity_at active_revision_id extra extra_ref_id extra_count marked 
and each line from  forum_users.tsv
id reputation gold silver bronze
Combine: 
reputation, gold, silver, and bronze medals 
for each author_id, with:
id title tagnmes author_id node_type parent_id abs_parent_id added_at score
for the same author id.

Throw away the body, and add "A" for the forum_users.tsv, and "B" for the forum_node.tsv
This will cause the shuffle/sort to put the forum_user.tsv line at the beginning of each 
user id section. 
Output for forum_user is: author_id A reputation gold silver bronze
Output for forum_node is: author_id B id title tagnmes author_id node_type parent_id abs_parent_id added_at score
The reducer will use this structure to speed things up.
'''

import sys, csv, string

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if line[0]=="id" or line[0]=="user_ptr_id":
		print 'skip'
		continue
	elif len(line)==5:
		lineout = string.join([line[0],"A"],"\t")
		for entry in line[1:]:
			lineout = string.join([lineout, entry],"\t")
		print lineout
	elif len(line)==19:
		line.pop(4)
		lineout = string.join([line[3],"B"],"\t")
		for entry in line[0:9]:
			lineout = string.join([lineout, entry],"\t")
		print lineout

