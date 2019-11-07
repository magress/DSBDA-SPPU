#!/usr/bin/python
import sys

for line in sys.stdin:
	val = line.strip().split(',')
	#print(val[0],val[1])
	
	(month,day,temp) = (val[2],val[3],val[8])

	print "%s\t%s\t%s" % (month,day,temp)
	
