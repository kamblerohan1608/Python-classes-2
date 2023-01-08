class A:
    def m1(self):
        self.grandfather = "Grandfather"
    def get_m1(self):
        return self.grandfather
class B(A):
    def m2(self):
        self.father = "Father"
    def get_m2(self):
        return self.father
class c(B):
    def m3(self):
        self.child = "Child"
    def get_m3(self):
        return self.child
    def get_all_pro(self):
        self.gf = self.get_m1()
        self.f = self.get_m2()
        self.ch = self.get_m3()
        return [self.gf,self.f,self.ch]

obj = c()
obj.m1()
obj.m2()
obj.m3()
all_pr = obj.get_all_pro()
print(obj.get_all_pro())