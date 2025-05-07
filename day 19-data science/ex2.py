import numpy as np
marks = np.array([[45, 56, 78, 90, 65,],[90, 41, 54, 63, 77]])
print(marks.dtype)
print(marks.sum())
print(marks.sum(axis=0))
print(marks.sum(axis=1))

print(np.sqrt(marks))

numbers=np.arange(1,11)
numbers2=np.arange(11,21)
numbers3=np.add(numbers,numbers2)
print(numbers3)
print(numbers*2)
marks = np.array([[45, 56, 78, 90, 65,],[90, 41, 54, 63, 77],[69,81,57,67,48]])

print(marks[[0,2],3])
# for i in marks:
#     for j in i:
#         print(j,end="" "\n")

# numbers=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# evenNumbers = [num for num in range(len(numbers)) if num % 2 == 0]
# print(evenNumbers)




"""create a one dimensional array from a list comprehension that produce the even integers from 2 to 20"""