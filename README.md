## This is a repository with simple Hadoop/MapReduce routines 

All mappers and reducers are written in Python and use the Hadoop Python streaming API. 
The code produced the expected results on the Cloudera-Udacity Virtual machine, distributed 
at the [Udacity course website](https://www.udacity.com/wiki/ud617#virtual-machine). 

There is a corresponding blog post for a small subset of this work [here](http://nikosd.me/jekyll/update/2014/10/13/Map-Reduce:-21st-century-Lemmings.html) and [here](http://oligotropos.wordpress.com/2014/10/13/mapreduce-lemmings-in-the-21st-century/).

Data
----

The data on which the code runs is also available at the course website 
([access log]( http://content.udacity-data.com/courses/ud617/access_log.gz), 
[purchases.txt]( http://content.udacity-data.com/courses/ud617/purchases.txt.gz),
[udacity forum data](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz))

### 1. Access log

This is the access log of webserver in Common Log Format:

	`10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469`

Or:

	%h %l %u %t \"%r\" %>s %b

Where:

    %h is the IP address of the client
    %l is identity of the client, or "-" if it's unavailable
    %u is username of the client, or "-" if it's unavailable
    %t is the time that the server finished processing the request. The format is `[day/month/year:hour:minute:second zone]`
    %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
    %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
    %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.

### 2. Purchase log

This is a file containing information on purchases made in a number of stores. Each line in purchases.txt consists of tab delimited entries:

date\ttime\tstore name\titem description\tcost\tmethod of payment

e.g.
 
2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex

### 3. Udacity forum data

This is data from the udacity forum (similar to Stack Exchange format). 
There are two files. Each line in `forum_node.tsv` has the following fields:

	id title tagnames author_id body node_type parent_id abs_parent_id added_at score state_string last_edited_id last_activity_by_id last_actitvity_at active_revision_id extra extra_ref_id extra_count marked 

Each line in `forum_users.tsv` has the following fields:

	id reputation gold silver bronze



Code
----

In what follows, the mapper and reducer functions are organized according to the type of operation they perform. 

For each mapper and reducer, I am also specifying the input and output files as in:
(`input file` -> `mapper.py`, `reducer.py` -> `output file`)

### 1. Summarization patterns

* Find the total sales amount for each store
	(`purchases.txt` -> `mapper0.py`,`reducer0.py` -> `part-00000`)
* Break down the sales by category, and find total sales for each category, e.g. Toys 
	(`purchases.txt` -> `mapper1.py`,`reducer1.py` -> `part-00001`)
* Find the total number of sales and the total sales value from all the stores 
	(`purchases.txt` -> `mapper3.py`, `reducer3.py` -> `part-00003`)
* Find the number of hits to /assets/js/the-associates.js 
	(`access.log` -> `mapper4.py`, `reducer4.py` -> `part-00004`)
* Find the number of hits to the IP 10.99.99.186 
	(`access.log` -> `mapper5.py`, `reducer5.py` -> `part-00005`)
* Create an inverted index of the words found in the body of each node of the forum, i.e. index word, nodeid_1, nodeid_2, ... 
	(`forum_node.tsv` -> `mapper9.py`, `reducer9.py` -> `part-00009` -not included due to size limit)
* Find the mean number of sales for each day of the week 
	(`purchases.txt` -> `mapper10.py`, `reducer10.py` -> `part-00010`)
*  Find the sum of sales for each day of the week, using combiners at the mappers
	(`purchases.txt` -> `mapper11.py`, `reducer11.py` -> `part-00011`)
* Find the length of each question and the average length of the answers to that question
	(`test_posts.tsv` -> `mapper13.py`, `reducer13.py` -> `test-out-00013` )

### 2. Filtering patterns

* Find all forum entries containing a single sentence in their body
	(`forum_node.tsv` -> `mapper7.py` -> `part-00007`).
* Find the value of the highest individual sale for each separate store 
	(`purchases.txt` -> `mapper2.py`,`reducer2.py` -> `part-00002`)
* Find the most popular file on the website, and the number of times it appears in the log 
	(`access.log` -> `mapper6.py`, `reducer6.py`, `part-00006`)
* Print the top 10 longest posts in ascending order, shortest to longest (top-N pattern, using mapper only)
	(`forum_node.tsv` -> `mapper8.py` -> `part-00008`)
* Find which students have posted under threads with the same tag
	(`test_posts.tsv` -> `mapper14.py`, `reducer14.py` -> `test-out-00014`)
* Find at what time of the day each student has the largest number of posts
	(`test_posts.tsv` -> `mapper15.py`, `reducer15.py` -> `test-out-00015`)
* Find the top 10 tags ordered by the number of questions submitted under a tag
	(`test_posts.tsv` -> `mapper16.py`, `reducer16.py` -> `test-out-00016`)

### 3. Structural patterns

* Combine two data sets from two different input files.
	(`forum_node.tsv`, `forum_users.tsv` -> `mapper12.py`, `reducer12.py` -> `part-00012`)

