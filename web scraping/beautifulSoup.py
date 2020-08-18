from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
#ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_node = ssl.CERT_NONE

# url=input('Enter-')
url='http://www.dr-chuck.com/page1.htm'
# url2='http://www.dr-chuck.com/page2.htm'
html=urllib.request.urlopen(url , context=ctx).read()
# Read reads the whole file
soup = BeautifulSoup(html , 'html.parser')
# Soup cleans the things

# Retrieve all of the anchor tags
tags=soup('a')
# This can be also said as a question asked to Soup
for tag in tags:
	print(tag.get('href',None))