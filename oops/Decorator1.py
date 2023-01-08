# Decorator :- it can modify the function from outside without doing any changes in the function.

#Example 1

# def decor_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner

# @decor_div
# def div(a,b):
#     return a/b

# print(div(10,2))
# print(div(2,10))

# Example 2

def decor_per(func):
    def inner(obtain,total):
        if obtain > total:
            obtain,total = total,obtain
        return func(obtain,total)
    return inner

@decor_per
def per(obtain,total):
    return (obtain*100)/total

print(per(10,2))
print(per(2,10))
