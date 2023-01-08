'''
#hollow pyramid
#static

row=1
while row<=5:
    col=1
    while col<=9:
        if row==5 or row+col==6 or col-row==4:
            print("*",end=" ")
        else:
            print(" ", end=" ")
        col+=1
    row+=1
    print()

#dynamic

a=int(input("Enter the height of pyramid : "))
row=1
while row<=a:
    col=1
    while col<=(a*2)-1:
        if row==a or row+col==a+1 or col-row==a-1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
        col+=1
    row+=1
    print()

'''

row=1
while row<=9:
    col=1
    while col<=6:
        if row==1 and col>1 and col<6:
            print("*",end=" ")
        elif col==1 and row>1 and row<5:
            print("*",end=" ")
        elif row==5 and col>1 and col<6:
            print("*",end=" ")
        elif col==6 and row>5 and row <9:
            print("*",end=" ")
        elif row==9 and col>1 and col<6:
            print("*",end=" ")
        elif (row==8 and col==1) or (row==2 and col==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
























