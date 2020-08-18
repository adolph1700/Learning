import re

hand=open('actualTest.txt')
sumOfNumbers=0
for line in hand:
	tline=line.rstrip()
	y=re.findall('[0-9]+',tline)
	if len(y)!=0:
		for num in y:
			sumOfNumbers+=int(num)
print(sumOfNumbers)