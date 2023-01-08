weight = float(input("Enter the weight in kg : "))
height = float(input("Enter the height in cm : "))
bm=weight/(height/100)**2
bm1=round(bm,2)
print("The Body Mass Index is : ",bm1)
