
# with cunstructor

class A:
    def __init__(self):
        self.name = "Rohan"

class B(A):
    def __init__(self):
        self.age = 45
        super().__init__()


class C(A):
    def __init__(self):
        self.loction = "Mumbai"
        super().__init__()

        


def main():
    obj_B = B()
    obj_C = C()
    print(obj_B.name)
    print(obj_B.age)
    print(obj_C.name)

main()