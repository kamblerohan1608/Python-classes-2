
# Generator Function

# Generator object is returned when yeild is used 

# used if multiple values are to be returned 

# Also after using once data inside generator object get vanished.   

def fact(n):
    f = 1
    for i in range(n,0,-1):
        f = f * i
        yield f

x = fact(5)
print(x)
y = list(x)
print(y)
print(x)
