'''
Week6 assignment1:
------------------------------------------------------------------------------
Author: MiracleZhang 
Date: April, 2016
------------------------------------------------------------------------------
'''
import json
import urllib

json_url = raw_input("Enter Location:")
print "Retrieving", json_url
json_uh = urllib.urlopen(json_url)
readData = json_uh.read()
data = readData.decode()
print 'Retrieved', len(data), 'characters'
json_data = json.loads(data)

sum = 0
totalNum = 0



for item in json_data["comments"]:
    sum += int(item["count"])
    totalNum += 1

print 'Count: ', totalNum 
print 'Sum: ', sum