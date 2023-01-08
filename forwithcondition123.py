# take input from user and dispay invalid to value above 50
'''
a=int(input("Enter the number : "))
if a>0 and a<=50:
    for i in range(1,a+1):
        print(i)
else:
    print("invalid number out of range.")
'''

#take a list and check whether a is present in it or not:
'''
ls=["Rohan","Sam","Rishi","Suraj","Sagar","Kirti","jhon","Sherlok"]
for i in ls:
    if "a" in i:
        print("a is present in "+ i)
    else:
        print("a is not present in" +i)
'''
#take a lst of numbers amd display thr even numbers in it:
'''
ls=[1,34,56,33,86,56,12,666,488,598,177,745,6,4,126,1025]
total=0
for i in ls:
    if i%2==0:
        print("The entered number is even", i)
        total=total+1
    else:
        print("The entered number is odd", i)
print("The total even numbers in list are : ",total)
'''
for i in range(4):
    for j in range(4):
        print(j)
    print(i)

