# lastModified
#"This file print the LAST MODIFIED DATA of the given WEBSITE"
import urllib2
def getLast(url):
	request = urllib2.Request(url)
	opener = urllib2.build_opener()
	firstdatastream = opener.open(request)
	headVal=firstdatastream.headers.dict
	lastMod=firstdatastream.headers.get("last-modified")
	
	return headVal, lastMod

print "This file print the LAST MODIFIED DATA of the given WEBSITE"
getVal=raw_input("Enter URL for Last modified:")
head,lastMod=getLast(getVal)
print lastMod
