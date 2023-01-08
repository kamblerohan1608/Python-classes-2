# single inheritance without parameters

class A:
    def __init__(self):
        self.stu_name = "Rohan"
        self.stu_age = 16
        self.stu_roll = 21
        self.stu_location = "Mumba"
        self.stu_contact = 2698754125

    def test(self):
        print("This is a test method for class A")

class B(A):
    def __init__(self):
        self.emp_name = "Kishor"
        self.emp_location = "Thane"
        self.emp_id = 123
        self.emp_contact = 6549862654
        super().__init__()

    def test1(self):
        print("This is a test method for class B")

obj = B()
print("Employ number : ", obj.emp_contact)
print("Employ name : ",obj.emp_name)
print("Student name : ",obj.stu_name)
