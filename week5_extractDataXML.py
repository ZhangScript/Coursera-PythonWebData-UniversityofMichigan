'''
Week5 assignment:
------------------------------------------------------------------------------
Author: MiracleZhang 
Date: April, 2016
------------------------------------------------------------------------------
'''

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
#  http://python-data.dr-chuck.net/comments_42.xml

total_number = 0
sum = 0

print('Retrieving', url)
uh = urllib.urlopen(url)
data = uh.read()	
print'Retrieved', len(data), 'characters'

tree = ET.fromstring(data)
nums = tree.findall('.//count')

for num in nums:
    sum += int(num.text)
    total_number += 1

print "Count: ", total_number
print "Sum: ", sum
