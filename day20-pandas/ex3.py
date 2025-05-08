import pandas as pd 
grades_dict = {"Tom": [87, 96, 70], "Diana": [99, 78, 90], "Fred": [100, 99, 78], "Bob": [89, 81, 83]}
gradesDF = pd.DataFrame(grades_dict,index=["java","python","c#"])
# print(gradesDF[["Diana"]])
# print(gradesDF.loc["python":"c#"])
# print(gradesDF.iloc[0:2])
# print(gradesDF.loc["java":"c#","Diana":"Fred"])
# print(gradesDF[(gradesDF>=80)&(gradesDF<90)])#between above 80 but less than 90
# print(gradesDF[gradesDF>90])

# print (gradesDF.mean(axis=1))
# print(gradesDF.describe())#summary
print(gradesDF.sort_index(ascending=False))