class A:
    def test(self):
        print("Parent car is Hounda Citi")
class B(A):
    def test(self):
        super().test()
        print("Child car is Kia")
        

obj=B()
obj.test()