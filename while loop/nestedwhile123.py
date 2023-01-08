# nested while :
'''
#1

i=1
while i<=4:
    j=1
    while j<=4:
        print("inner loop ",j)
        j+=1
    print("outer loop",i)
    i+=1

#2

i=1
j=1
while i<=4:
    while j<=4:
        print("inner loop",j)
        j+=1
    print("outer loop",i)
    i+=1
    

#3


i=1
while i<=4:
    j=1
    while j<=4:
        print("inner loop",j)
        j+=1
        i+=1
    print("outer loop",i)
    


* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

n=5
row=1
while row<=n:
    col=1
    while col<=n:
        print("*",end=" ")
        col+=1
    print()
    row+=1



* 
* * 
* * * 
* * * * 
* * * * *

n=5
row=1
while row<=n:
    col=1
    while col<=row:
        print("*",end=" ")
        col+=1
    print()
    row+=1



* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

n=5
row=1
while row<=n:
    col=1
    while col<=row:
        print("*",end=" ")
        col+=1
    print()
    row+=1
row=4
while row>=1:
    col=1
    while col<=row:
        print("*",end=" ")
        col+=1
    row-=1
    print()

'''





















































