class A:
    def __init__(self):
        self.grandfather = "Grandfather"
    def m1(self):
        return self.grandfather
class B(A):
    def __init__(self):
        self.father="Father"
        super().__init__()
    
    def m2(self):
        return self.father
class C(B):
    def __init__(self):
        self.child = "child"
        super().__init__()
    def m3(self):
        return self.child
    def all_pro(self):
        return [self.m1(),self.m2(),self.m3()]




obj = C()
obj.m1()
obj.m2()
obj.m3()

print(obj.all_pro())

