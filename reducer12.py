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

The data fed from the markers will be in the format key\tval\tval...
with form
author_id A reputation gold silver bronze
or form
author_id B id title tagnmes author_id node_type parent_id abs_parent id added_at score

When the key (user id) changes the first line is always a line key\tA\t...
Save this line in currentUser, remove the A and append the value to each new entry with the same auth_id, after removing B from it 
'''

import sys, string

currentUser = None
part1 = None
part2 = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped)==6 and data_mapped[1]=="A" and currentUser!=data_mapped[0]:
		currentUser = data_mapped[0]
		part2 = data_mapped[2:]
	elif len(data_mapped)==11 and data_mapped[1]=="B" and currentUser==data_mapped[0]:
		part1 = data_mapped[2:]
		part1.extend(part2)
		lineout = string.join(part1,"\t")
		print lineout
	else:
		# Something has gone wrong. Skip this line.
		continue


