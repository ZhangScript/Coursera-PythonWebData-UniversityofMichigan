'''
Week6 assignment2:
------------------------------------------------------------------------------
Author: MiracleZhang 
Date: April, 2016
------------------------------------------------------------------------------
'''
import urllib
import urllib
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"
# This API only accepts the university in a list of its accepted ones.
# This API uses the same parameters (sensor and address) as the Google API.
# This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.

address_input = raw_input("Enter location: ")
params = {"sensor": "false", "address": address_input}
url = serviceurl + urllib.urlencode((params))
print"Retrieving ", url
json_uh = urllib.urlopen(url)
readData = json_uh.read()
data = readData.decode()
print'Retrieved', len(data), 'characters'
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print "Place id", place_id

