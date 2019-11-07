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
	value = line.strip().split("\t")
	
	key1.append(int(value[0]))
	key2.append(int(value[1]))
	val.append(int(value[2]))

df = pd.DataFrame({'year': key1, "month": key2, "val": val})

df_max = df.groupby(['year', 'month'])['val'].max()
print(df_max)

df_min = df.groupby(['year', 'month'])['val'].min()
print(df_min)