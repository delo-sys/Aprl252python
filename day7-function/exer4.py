def calc_average(test1, test2, test3,test4,test5):
    return (test1 + test2 + test3 + test4 + test5) / 5

def determine_grade(test):
    if(test < 0 or test > 100):
        print("error not a valid")
        
    elif test >= 90:
        return "A"
    elif test >= 80:
        return "B"
    elif test >= 70:
        return "C"
    elif test >= 60:
        return "D"
    else:
        return "F"
def main():
    test1 = float(input("Enter the score for Test 1: "))
    test2 = float(input("Enter the score for Test 2: "))
    test3 = float(input("Enter the score for Test 3: "))
    test4 = float(input("Enter the score for Test 4: "))
    test5 = float(input("Enter the score for Test 5: "))

    print (f"grade Test 1 is {determine_grade(test1)}")
    print (f"grade Test 2 is {determine_grade(test2)}")
    print (f"grade Test 3 is {determine_grade(test3)}")
    print (f"grade Test 4 is {determine_grade(test4)}")
    print (f"grade Test 5 is {determine_grade(test5)}")

    average = calc_average(test1, test2, test3,test4,test5)
    print ("The average  score is ",average)
    determine_grade(average)

main()