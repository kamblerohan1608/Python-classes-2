
print()
print()
print()
print("1- Addition")
print("2- Substraction")
print("3- Multiplication")
print("4- Division")
print("5- Percentage")
print("6- Factorial")
print("7- Addition")
print()
print()
while True:

    ch=int(input("Enter the choice : "))
    print()
    
    if ch==1:
        a=int(input("Enter the first number for addition : "))
        b=int(input("Enter the secound number for addition : "))
        print("The addition is ", a+b)
    elif ch==2:
        a=int(input("Enter the first number for substraction : "))
        b=int(input("Enter the secound number for substraction : "))
        print("The substraction is ", a-b)
    elif ch==3:
        a=int(input("Enter the first number for Multiplication : "))
        b=int(input("Enter the secound number for Multiplication : "))
        print("The multiplication is ", a*b)
    elif ch==4:
        a=int(input("Enter the first number for division : "))
        b=int(input("Enter the secound number for division : "))
        print("The division is ", a/b)
    elif ch==5:
        pass
    elif ch==6:
        pass
    elif ch==7:
        print("*******************Thank you******************")
        break
    else:
        print()
        print("******************invalid option***************************")
        print()
