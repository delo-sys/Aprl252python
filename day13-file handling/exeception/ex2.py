veges=["carrot","potato"]
try:
    print(veges[1])
except IndexError:
    print("Error-list index out of range")