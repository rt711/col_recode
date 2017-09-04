#!/usr/bin/python
import pandas as pd
import numpy as np
from tqdm import tqdm, tqdm_pandas

tqdm.pandas(desc="Processing dataframe")


df = pd.read_csv('data/pandas-test.csv')
df.columns

def recode_value(recoder):
     if recoder.startswith('aa'):
         return 'aanode'
     elif recoder.startswith('bb'):
         return 'bbnode'
     else:
         return np.nan

# print columns

df['xnodes'] = df.value1.progress_apply(recode_value, 'value1')

print(df)

val2_mean = df.value2.mean()
val2_max = df.value2.max()
print('value2 mean: ' + str(val2_mean))
print('value2 max: ' + str(val2_max))

print(df.columns)
droplist = ['value1']
df = df.drop(droplist, axis='columns')
print(df)
print(df.columns)
