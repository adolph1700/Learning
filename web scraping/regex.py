import re
# hand=open('mbox-short.txt')
str='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
email=" From yo@gmail.com fxcdf23 23 3"
# for line in hand:
# 	line=line.rstrip()
# 	if re.search('From:',line):
# 		print(line)
# 	if line.find('From:')>=0:
# 		print(line)


# 	if line.startswith('From:'):
# 		print(line)
# 	if re.search('^From:',line):
# 		print(line)

# ' . '  is any character * is any number of times
# ^ means at beginning
#^X.*:

# ^X-\S+:
#i.e \S+ is any non whitespace chractere 1 or more times

#[0-9] only 1 charcter in a range

# y=re.findall('[0-9]+',email)
# y=re.findall('[aeiou]',str)
# y=re.findall('^M.+:',str)
# * and + is greedy finds largest possible
# y=re.findall('^M.+?:',str)
# y=re.findall("\S+@\S+",str)
# y=re.findall(" From (\S+@\S+)",email)
# y=re.findall("@([^ ]*)",email)
# so ( is start extracting  and ) is stop
# y=re.findall("From .*@([^ ]*)",email)
# y=re.findall("@(\S+)",str)
# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
print(y)