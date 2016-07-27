'''
Week4 assignment1:
Scraping Numbers from HTML using BeautifulSoup
------------------------------------------------------------------------------
Author: MiracleZhang 
Date: April, 2016
------------------------------------------------------------------------------
'''


import urllib
from BeautifulSoup import *

url = raw_input('Enter the url to scrape - ')

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count_of_spans = 0
sum = 0

spans = soup('span')
for span in spans:
    sum += int(span.contents[0])
    count_of_spans += 1

print 'Count: ', count_of_spans
print 'Sum: ', sum
