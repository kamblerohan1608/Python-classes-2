
# function can be represented as a parameter of another function
# function can be represented as a return of another function
# function can be defined inside another function (Inner Function)

# Example 1

# def A():
#     def test():
#         print("Hello function")
#     return test

# a=A()
# a()

# Example 2

# # Using function as parameter (without parameter) 

# def add():
#     return 100+10
# def mul():
#     return 50*3

# def calc(function1,function2):
#     a=function1()
#     b=function2()

#     return(a+b)

# print(calc(add,mul))

# Example 2

# Using function as parameter (with parameter)

def add(a,b):
    return a+b
def mul(p,q):
    return p*q

def calc(function1,function2,a,b,p,q):
    A=function1(a,b)
    B=function2(p,q)

    return(A+B)

print(calc(add,mul,10,10,10,10))