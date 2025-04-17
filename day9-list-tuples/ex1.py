zeroes=[0]*10
print(zeroes) 

range_list = list(range(1,11))
print(range_list)

range_list2 = list(range(100,95,-1))
print(range_list2)

x=len(range_list)
print(x)#length of the list or number of elements/item in the list

eacountries = ["Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi", "South Sudan"]
print(eacountries)
countries2=eacountries#does not create a copy of the list, it creates a reference to the same list
eacountries.remove("Burundi")
print(countries2)

copycountries=eacountries.copy()#creates a copy of the list
print(copycountries)

copycountries2=[]+eacountries#creates a copy of the list
copycountries3=[]
copycountries3 . extend(eacountries)#creates a copy of the list
print(copycountries3)