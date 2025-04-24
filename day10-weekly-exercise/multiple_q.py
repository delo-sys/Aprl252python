qns=["when did kenya gain independence,\nA:1963,\nB:1964",
    "what is your favorite hobby\nA:Reading,\nB:Traveling",
    "number of days in a week\nA:7,\nB:8"]

correct_ans=["A","B","A"]
point=0
for counter in range (len(qns)):
    print(qns[counter])
    given_ans=input()
    while given_ans.upper()!="A" and given_ans.upper()!="B":#input validation
        print("invalid input, please enter A or B")
        given_ans=(input())

    if given_ans.upper()==correct_ans[counter]:
        print("correct")
        point+=1
    else:
        print("incorrect")
        print(correct_ans[counter] + " is the correct answer")
        
print(f"you scored {point} out of {len(qns)}")