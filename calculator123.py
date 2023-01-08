
#calculator
'''
#example 1 calculate by choice (1- add,2- sub....)

print("Press 1 - Adition")
print("Press 2 - Substraction")
print("Press 3 - multiplication")
print("Press 4 - Division")
print("Press 5 - Percentage")

ch=int(input("Enter your choice : "))

if (ch ==1):
    a = int(input("Enter first number for addition : "))
    b = int(input("Enter secound  number for adition : "))
    print("The addition is : ",a+b)
elif (ch == 2):
    a = int(input("Enter first number for substraction : "))
    b = int(input("Enter secound  number for substraction : "))
    print("The substraction is : ",a-b)
elif (ch == 3):
    a = int(input("Enter first number for multiplication : "))
    b = int(input("Enter secound  number for multiplication : "))
    print("The multiplication is : ",a*b)
elif (ch == 4):
    a = int(input("Enter first number for division : "))
    b = int(input("Enter secound  number for division : "))
    print("The division is : ",a/b)
elif (ch == 5):
    a = int(input("Enter marks obtained : "))
    b = int(input("Enter the total marks : "))
    per = a/b*100
    print("The percentages are : ",round(per,2))
else:
    print("invalid input....Please enter valid choice.")
print("Program Finished.")


#exapmle 2 calculate by choice (either 1 = addition or add = addition)


print("Press 1 or add - Adition")
print("Press 2 or sub - Substraction")
print("Press 3 or mul - multiplication")
print("Press 4 or div - Division")
print("Press 5 or per - Percentage")

ch=input("Enter your choice : ")

if (ch =="1" or ch == "add"):
    a = int(input("Enter first number for addition : "))
    b = int(input("Enter secound  number for adition : "))
    print("The addition is : ",a+b)
elif (ch == "2" or ch =="sub"):
    a = int(input("Enter first number for substraction : "))
    b = int(input("Enter secound  number for substraction : "))
    print("The substraction is : ",a-b)
elif (ch == "3" or ch == "mul"):
    a = int(input("Enter first number for multiplication : "))
    b = int(input("Enter secound  number for multiplication : "))
    print("The multiplication is : ",a*b)
elif (ch == "4" or ch == "div"):
    a = int(input("Enter first number for division : "))
    b = int(input("Enter secound  number for division : "))
    print("The division is : ",a/b)
elif (ch == "5" or ch == "per"):
    a = int(input("Enter marks obtained : "))
    b = int(input("Enter the total marks : "))
    per = a/b*100
    print("The percentages are : ",round(per,2))
else:
    print("invalid input....Please enter valid choice.")
print("Program Finished.")
'''
#example 3 calculate by any relevent input by user


print("Press 1 or add - Adition")
print("Press 2 or sub - Substraction")
print("Press 3 or mul - multiplication")
print("Press 4 or div - Division")
print("Press 5 or per - Percentage")

ch=input("Enter your choice : ")
add=["1","add","Add","ADD","addition","Addition","ADDITION","+"]
sub=["2","sub","Sub","SUB","substraction","Substraction","SUBSTRACTION","-"]
mul=["3","mul","Mul","MUL","multiplication","Multiplication","MULTIPLICATION","*"]
div=["4","div","Div","DIV","division","Division","DIVISION","/"]
per=["5","per","Per","PER","percentage","Percentage","PERCENTAGE","%"]
if (ch in add):
    a = int(input("Enter first number for addition : "))
    b = int(input("Enter secound  number for adition : "))
    print("The addition is : ",a+b)
elif (ch in sub):
    a = int(input("Enter first number for substraction : "))
    b = int(input("Enter secound  number for substraction : "))
    print("The substraction is : ",a-b)
elif (ch in mul):
    a = int(input("Enter first number for multiplication : "))
    b = int(input("Enter secound  number for multiplication : "))
    print("The multiplication is : ",a*b)
elif (ch in div):
    a = int(input("Enter first number for division : "))
    b = int(input("Enter secound  number for division : "))
    print("The division is : ",a/b)
elif (ch in per):
    a = int(input("Enter marks obtained : "))
    b = int(input("Enter the total marks : "))
    per = a/b*100
    print("The percentages are : ",round(per,2),"%")
else:
    print("invalid input....Please enter valid choice.")
print("Program Finished.")
