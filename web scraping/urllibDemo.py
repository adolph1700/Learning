import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
#file handle
# dosen't gives Header
counts =dict()
for line in fhand:
	words = line.decode().strip()
	print(words)
	# for word in words:
	# 	counts[word] = counts.get(word, 0)+1
# print(counts)