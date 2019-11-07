#!/usr/bin/python
import sys
from operator import itemgetter
import numpy as np
import functools


for line in sys.stdin:
	(key,v1,v2,v3,v4,v5,v6,v7) = line.strip().split("\t")
	#print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (key,v1,v2,v3,v4,v5,v6,v7)
	
	list1 = [int(v1),int(v2),int(v3),int(v4),int(v5),int(v6),int(v7)]
	#print(list1)
	#print (functools.reduce(lambda a,b : a if a > b else b,list1))
	print ("%s\t%d" % (key,functools.reduce(lambda a,b : a if a > b else b,list1)))
