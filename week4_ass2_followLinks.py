'''
Week4 assignment2: 
Following Links in Python
In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
------------------------------------------------------------------------------
Author: MiracleZhang 
Date: April, 2016
------------------------------------------------------------------------------
The right answer for http://python-data.dr-chuck.net/known_by_Fikret.html:
Enter - http://python-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving:  http://python-data.dr-chuck.net/known_by_Fikret.html
Retrieving:  http://python-data.dr-chuck.net/known_by_Montgomery.html
Retrieving:  http://python-data.dr-chuck.net/known_by_Mhairade.html
Retrieving:  http://python-data.dr-chuck.net/known_by_Butchi.html
Last URL  http://python-data.dr-chuck.net/known_by_Anayah.html
------------------------------------------------------------------
The right answer for http://python-data.dr-chuck.net/known_by_Alyas.html:
Enter -  http://python-data.dr-chuck.net/known_by_Alyas.html 
Enter count: 7
Enter position: 18
Retrieving:   http://python-data.dr-chuck.net/known_by_Alyas.html 
Retrieving:  http://python-data.dr-chuck.net/known_by_Meko.html
Retrieving:  http://python-data.dr-chuck.net/known_by_Darla.html
Retrieving:  http://python-data.dr-chuck.net/known_by_Cain.html
Retrieving:  http://python-data.dr-chuck.net/known_by_Karyss.html
Retrieving:  http://python-data.dr-chuck.net/known_by_Mariena.html
Retrieving:  http://python-data.dr-chuck.net/known_by_Kade.html
Last URL  http://python-data.dr-chuck.net/known_by_Jodie.html
'''

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count_num = int(input('Enter count: '))
pos = int(input('Enter position: '))


def parseHtml(url, pos):     
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    i = 0
    for tag in tags:
        i += 1
        if i == pos:
            return tag.get('href', None)

current_num = 0
while current_num < count_num:
     print 'Retrieving: ', url
     url = parseHtml(url, pos)
     current_num += 1

print 'The Last URL of this turn:', url




     
