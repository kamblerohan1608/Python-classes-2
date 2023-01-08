# while loop
'''
i=1
while (i<=10):
    print(i)
    i=i+1
'''
#
'''
i=10
while (i>=1):
    print(i)
    i=i-1
'''
#
'''
a=int(input("Enter the number : "))
i=1
while (i<=a):
    print(i)
    i=i+1
'''
#
'''
a=int(input("Enter the number : "))
i=a
while (i>=1):
    print(i)
    i=i-1
    
#table

#a=int(input("Enter the number : "))
i=1
fac=1
n=5
while (i<=n):
    fac=fac*i
    print(fac)
    i=i+1
    
#factorial

a=int(input("Enter the number : "))
fact=1
i=1
while i<=a:
    fact=fact*i
    i=i+1
print(fact)

#
a=int(input("Enter the number : "))
i=1
if (a<=100) and (a>0):
    while i<=a:
        print(i)
        i=i+1
else:
    print("Entered number is out of range.")
'''
#
'''
a=int(input("Enter the number : "))

if (a>=-100) and (a<0):
    while a<=-1:
        print(a)
        a=a+1
else:
    print("Entered number is out of range.")
'''
#

a=int(input("Enter the number : "))
i=1
if (a<=100) and (a>0):
    while i<=a:
        print(i)
        i=i+1
elif (a>=-100) and (a<0):
    while a<=-1:
        print(a)
        a=a+1
else:
    print("Entered number is out of range.")











