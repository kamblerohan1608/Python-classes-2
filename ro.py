# relation operators

a=20
b=30
c=10

print("a < b : ",a<b) # true
print("a > b :",a>b) #false
print("c < a <b : ",c<a<b) #true

A=(a<b)
B=(b>c)
C=(c==a)

print(a<b and b>c) #true
print(A and B) #true
#print(A or C) #true


m=[1,2,3,4,5,6,7,8,9,10]
n=4
a=(n in m)
b=(n not in m)
print(a)
print(b)

