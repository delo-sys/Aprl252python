student = {"name": "John",
"age": 20,
"course": ["pthyon programming", "java","web design","c++"],
"nationality":"Usa"
}

# declaring a dictionary using a method constructor
driver=dict(name="John",dlclass="BCE",licenseno="11111")
# print(student["course"][1])
# print(driver["student"])
print(len(student))
del student["nationality"]
print(len(student))