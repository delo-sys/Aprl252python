#series is a one-dimensional array-like object that can hold any data type
#it is similar to a list or a dictionary
#it is a labeled array, meaning that each element in the series has an index
#it is similar to a dictionary in that it can hold different data types
#it is similar to a list in that it is a one-dimensional array-like object
#it is similar to a numpy array in that it is a one-dimensional array-like object
#it is similar to a dataframe in that it is a one-dimensional array-like object
#and is labeled with an index
import numpy as np
import pandas as pd

#creating and storing values in a series
grades = pd.Series([87,100,94])
# print(grades[0])
# print(grades.mean())average
# print(grades.max())maximum
# print(grades.min())minimum
# print(grades.std())#standard deviation
# print(grades.var())#mode
# print(grades.median()) #median
# print(grades.describe()) #summary statistics
grades2=pd.Series([90,77,94],index=["Tom","Mary","joseph"])#creating a series with custom index
#assigning labels to the list in a series
# print(grades2["Tom","Mary"])
dictgrades={"java":87,"python":93,"c#":79}
grades3=pd.Series(dictgrades)
print(grades3)
# creating a series from a range of values
# hundreds=pd.Series(100,range(10))
# print(hundreds)
