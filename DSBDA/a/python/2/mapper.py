#!/usr/bin/python
import sys

for line in sys.stdin:
	val = line.strip().split('\t')
	#print(val[0],val[1])
	
	(name,v1,v2,v3,v4,v5,v6,v7) = (val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7])

	print ("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (name,v1,v2,v3,v4,v5,v6,v7))
	
