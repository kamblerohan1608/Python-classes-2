
#program 1:

#1

# greatest number among 4 numbers :

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))
d=int(input("Enter the number : "))

if (a>b):
    if (a>c):
        if (a>d):
            print(a," is greater.")
        else:
            print(d,"is greater.")
elif (b>c):
    if (b>a):
        if (b>d):
            print(b,"is greater.")
        else:
            print(d,"is greater.")
                            
elif (c>d):
    if (c>b):
        if (c>a):
            print(c,"is greater.")
        else:                               
            print(a,"is greater.")
else:
    print(d,"is greater.")



'''
#program 1:

#2


a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))
d=int(input("Enter the number : "))
if (a>b) and (a>c):
        if(a>d):
            print(a," is greater.")
        else:
            print(d,"is greater.")
elif (b>a) and (b>c):
        if (b>d):
            print(b,"is greater.")
        else:
            print(d,"is greater.")
elif (c>a) and (c>b):
        if (c>d):
            print(c,"is greater.")
        else:
            print(d,"is greater")
else:
    print(d,"is greater.")
    
'''
