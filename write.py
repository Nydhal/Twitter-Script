import numpy as np
import pandas as pd

# Read userlist into pandas (0-based) dataframe, column = id (64-bit unsigned integer)
result = pd.read_csv("resultlisttest.txt",sep=None)

idlist = pd.read_csv("userlist.txt",sep='\n', dtype=int)

print(result)
print("result.dtypes= ",result.dtypes)
print("result.columns= ",result.columns)

print(idlist)
print("result.dtypes= ",idlist.dtypes)
print("result.columns= ",idlist.columns)

# Merge twp data frames
new = pd.merge(idlist, result,how='left', on='id')
new.to_csv("resultlist.txt")

print(new)
print("result.dtypes= ",new.dtypes)
print("result.columns= ",new.columns)
print(new.isnull().sum())


