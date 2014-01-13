#Examples & excersises from Python for Data Analysis by Wes McKinn
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, draw, show
from collections import Counter
from pandas import DataFrame, Series
import pandas as pd

#Manipulation data without pandas as a start:

path = 'chapter2_data1_govData.txt'
#List comprehension - applies an operation (like json.loads) to
#a collection of strings or other objects
#Here the result is a python dict
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
	counts = {}
	for x in sequence:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1
	return counts

#counts = get_counts(time_zones)

#Alternatively use python standard lib's collections.Counter
counts = Counter(time_zones)

def top_counts(count_dict, n=10):
	value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
	value_key_pairs.sort() #convenient!
	return value_key_pairs[-n:] #Hmm. what does -n: mean? n = 10, but hmm.

#top_counts(counts)
counts.most_common(10)

#print counts

#Using pandas to do the same as above!
frame = DataFrame(records)
#print frame
tz_counts = frame['tz'].value_counts()
#print tz_counts[:10]

clean_tz = frame['tz'].fillna('Missing') #replaces NA values
#Use boolean array indexing to replace the empty strings with the string 'Unknown'
clean_tz[clean_tz == ''] = 'Unknown'

tz_counts = clean_tz.value_counts()
#print tz_counts[:10]

#Making horizontal bar plot using the plot method on the counts objects:
chart = tz_counts[:10].plot(kind='barh', rot=0)
#Must add show() if not it will not display anything!
#show()

results = Series([x.split()[0] for x in frame.a.dropna()])
#print results[:5]
os_counts = results.value_counts()[:8]

chart2 = os_counts[:10].plot(kind='barh', rot=0)
#show()

#Exclude from data values that are nll
cframe = frame[frame.a.notnull()]
#Computes value wheter each row is Windows or not:
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)

#Select top overall time zones by constructing an indirect index array from the
#row counts in agg_counts
indexes = agg_counts.sum(1).argsort()

#Use take to select the rows in that order, and slice off the last 10 rows:
count_subset = agg_counts.take(indexes)[-10:]
print count_subset

#count_subset.plot(kind='barh', stacked=True)
#Normalize to sum up to 1 and plot again to make it easier to see relative percentage
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
show()