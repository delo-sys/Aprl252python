# lamda arguments: expression

def tripler(n):# ordinary name function
    return n*3

print(tripler(20))

tripler2=lambda x: x*3 
print(tripler2(20))

print ((lambda x:x*3)(25))
print ((lambda x,y:x*y)(10,20))
print ((lambda x,y:x*y)(60,80))
print ((lambda x,y:x+y)(100,200))
print ((lambda x,y:x**y)(100,20))
print ((lambda x,y:x/y)(100,20))