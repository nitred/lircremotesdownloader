'''
Currently Ignores subfolders. There is only one such instance where there
is a subfolder with one remote control model in it.
'''
from lxml import html
import os
from bs4 import BeautifulSoup
import urllib
import urllib2

# The directory in which you want all the remote files to be downloaded to
remotedir = "c:/Python27/testcodes/lirclxmltest/"
# The lirc remotes library url
baseurl = "http://lirc.sourceforge.net/remotes/"
soup = BeautifulSoup(urllib2.urlopen(baseurl),"lxml")
#Counter for Company Number
count1 = 0
#Skipping first 5 <a> tags which are irrelevant; Subject to change
for link in soup.find_all('a')[5:]:
    count1 += 1       
    newurl = baseurl + link.get('href')
    print str(count1) + " : " + newurl

    newpath = remotedir + link.get('href')
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    remotes = BeautifulSoup(urllib2.urlopen(newurl),"lxml")
    #Counter for Remote Models inside a company name
    count2 = 0
    #Skipping first 5; non related links
    for remote in remotes.find_all('a')[5:]:
        count2 += 1
        #Ignoring directories; but the host is very accomodating
        if(remote.get('alt') == "[DIR]" or remote.get('href')[-1] == "/"):
            continue
        
        finurl = newurl + remote.get('href')
        print str(count2) + " - " + finurl

        #if(finurl[-4:] == '.jpg'):
        #   print "Skipping JPG"
        #   continue

        newpathfile = newpath + remote.get('href')

        urllib.urlretrieve(finurl,newpathfile)
    
    # uncomment this break to test if it works on the first run. Comment to run it full.
    #break
