import pandas as pd
import numpy as np

# Series1=pd.Series(np.random.random(4))
# Series2=pd.Series([2,3,4,5,3.4,"hii"])
# print(Series1)
# print(Series2)
# print(Series1.index)

# dict={'m':1,'y':2024,'d':"Sunday"}
# Series3=pd.Series(dict)
# print(Series3)
# S4=pd.Series(dict,index=['y','m','d','d1'])
# print(S4)

# S1=pd.Series(np.random.randn(4),index=['a','b','c','d'])
# print(S1)
# print(S1['c'])
# print(S1[1])

                         # CREATE A LIST FROM SCALAR VALUE

# scl=pd.Series(8,index=['a','b','c','d'])
# print(scl)

# Series1=pd.Series(np.random.random(4))
# print('Series1')
# print(Series1)
# print('\n mean',Series1.mean())
# print('\n median',Series1.median())
# print('\n max',Series1.max())
# print('\n min',Series1.min())
# print('\n Standard Deviation',Series1.std())
# print('\n sum',Series1.sum())

# S2=pd.Series([1,24,2,3,5,78])
# print(S2.sort_values())
# print(S2.sort_index())

                                        # MATHETICAL OPERATIONS
# S1=pd.Series([2,3,4,6,7])
# S2=pd.Series([1,2,3,5,78])
# print(S1+S2)
# print(S1[1:]+S2[:-1]) 
# print(S1**2)
# print(S1/S2)
# print(S1.apply(np.sqrt))
# print(S1.cumsum())                   # CUMULATIVE SUM
# print(S1.cumprod())                  # CUMULATIVE PRODUCT

# s=pd.Series([2,3,4,6,7],index=[1,2,34,5,6])
# print(s.index)
# print(s.values)
# print(s.dtype)
# print(s.size)
# print(s.shape)
# print(s.is_unique)

# s=pd.Series([2,3,4,None,7],index=[1,2,34,5,6])
# print(s.isnull())
# print(s.notnull())

# s=pd.Series([1,2,3,4],index=['a','b','c','d'])
# print(s)
# print(s['b':'d':2])
# print(s[1:3:2])