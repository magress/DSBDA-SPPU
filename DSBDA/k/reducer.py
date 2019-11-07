#!/usr/bin/python
import sys
from operator import itemgetter
import numpy as np
import functools
import pandas as pd

key1=[]
key2=[]
val=[]

for line in sys.stdin:
	(month,day,temp) = line.strip().split("\t")
	
	key1.append(month)
	key2.append(day)
	val.append(temp)

df = pd.DataFrame({'month': key1, "day": key2, "val": val})

df = df.groupby(['month', 'day'])['val'].max()

print(df)