import pandas as pd 
grades_dict = {"Tom": [87, 96, 70], "Diana": [99, 78, 90], "Fred": [100, 99, 78]}
# Create a DataFrame
gradesDF = pd.DataFrame(grades_dict,index=["java","python","c#"])
print(gradesDF)
gradesDF2 = pd.DataFrame(
	[[87, 96, 70], [99, 78, 90], [100, 99, 78], [89, 81, 83], [89, 81, 83]],
	columns=["java", "python", "c#"],
	index=["Tom", "Diana", "Fred", "Alice", "Bob"]
)
print(gradesDF2)
gradesDF3=pd.DataFrame(gradesDF2.T)
print(gradesDF3)
# gradesDF2.columns=["java","python","c#"]
# print(gradesDF2)