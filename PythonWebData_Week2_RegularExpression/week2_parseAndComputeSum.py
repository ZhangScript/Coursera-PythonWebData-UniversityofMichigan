'''
Week2 assignment: 
Extracting Data With regular expression
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.
------------------------------------------------------------------------------
Author: MiracleZhang 
Date: April, 2016
----------------------------------------------------------------------
The right answer for my week2_sampleSum42.txt:
There are 87 values with a sum= 445822.0
-----------------------------------------------------------------------
the right answer for my week2_assignment.txt is that:
There are 74 values with a sum= 354473.0
---------------------------------------------------------------------
This is a rather esay assignment for parse the data. 
'''

import re
## change the name to your target file 
hand = open ('week2_sampleSum42.txt')
numlist = list();
times = 0

for line in hand:
	## use regular expression 
	stuff = re.findall('[0-9]+',line)
	num = 0
	if len(stuff) == 0 : continue
	for str in stuff:
		num += float(str)
		times += 1
	numlist.append(num)

print 'There are', times, 'values with a sum=', sum(numlist)