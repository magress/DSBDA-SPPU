#!/usr/bin/python
import sys

for line in sys.stdin:
	val = line.strip().split(',')
	#print(val[0],val[1])
	
	(year,month,temp) = (val[1],val[2],val[3])

	print "%s\t%s\t%s" % (year,month,temp)
	
