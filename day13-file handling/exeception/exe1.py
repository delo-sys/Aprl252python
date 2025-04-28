from random import randint
randomnum=int(input("Enter the number of random numbers"))

try:
    f=open(r'C:\Users\Student\Documents\Aprl252python\day13-file handling\Random_number.txt','w')
    for counter in range(randomnum):
        randomnum=randint(1,501)
        f.write(str(randomnum)+"\n")
except:
    print("An Error occurred ")

