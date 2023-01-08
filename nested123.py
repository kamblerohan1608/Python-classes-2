
#nested if
'''
#identify number is positive, negative or zero

a=int(input("Enter the number : "))
if (a>=0):
    if(a>0):
        print("Entered number",a,"is positive")
    else:
        print("Entered number",a,"is zero")
else:
    print("Entered number is negative.")


#Example 2:

#percentage calculator

obtain = int(input("Enter the marks obtained : "))
total = int(input("Enter the total marks : "))
per = obtain/total*100
print("Your percentages are :",per,"%")
print("program finished")

#Example 2 (using nested if)


obtain = int(input("Enter the marks obtained : "))
total = int(input("Enter the total marks : "))
if (total >= 0) and (obtain >= 0):
    if (total < obtain):
        total,obtain = obtain,total
    per = obtain/total*100
    print("Your percentages are : ",per,"%")
else:
    print("Entered number is negative. ")

#Example 3

#Find the greates of 3 number entered by user

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the secound number : "))
num3 = int(input("Enter the third number : "))
if(num1 > num2) and(num1 > num3):
    print(num1,"is greated of all the numbers.")
elif(num2 > num1) and (num2 > num3):
    print(num2,"is greatest of all the numbers.")
else:
    print(num3,"is greatest of all numbers.")
'''

#Example 3 using nested

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the secound number : "))
num3 = int(input("Enter the third number : "))
if (num1 > num2):
    if (num1 > num3):
        print(num1,"is greatest of all entered numbers.")
    else :
        print(num3,"is greatest of all entered numbers.")
else :
    if(num2 > num3):
        print(num2,"is greatest of all entered numbers.")
    else:
        print(num3,"is greatest of all entered numbers.")
    


















    
















