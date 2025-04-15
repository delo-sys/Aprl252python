def sum(*nums):
    total= 0
    for x in nums:
        total = total + x
    return total
print(sum(2,8,4,5,6,7,8,9,10))