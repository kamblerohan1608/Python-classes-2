
# Hash A relation

class A:
    dept = "Tester"
    def __init__(self):
        self.name = "Rohan"
        self.age = 23 
    def m1(self):
        print(self.name,self.age)

class B:
    def __init__(self):
        self.salary = 40000
        self.loc = "Dadar"
        self.a = A()              # calling A function in B class
    def m2(self):
        print(self.salary,self.loc)

c = B()
print(c.a.name)
c.a.m1()