'''
# with constructor 
class A:
    def __init__(self):
        self.stu_name = "Rohan"
        
class B:
    def __init__(self):
        self.tec_name = "Madhu"
class C(A,B):
    def __init__(self):
        self.sch_name = "DBS"
        super().__init__()
        B.__init__(self)
obj = C()
print("Student name is : ",obj.stu_name)
print("Teacher name is : ",obj.tec_name)
print("school name is : ",obj.sch_name)
'''

# with constructor with parameter

class A:
    def __init__(self,stu_name):
        self.stu_name = stu_name
class B:
    def __init__(self,tec_name):
        self.tec_name = tec_name
class C(A,B):
    def __init__(self,sch_name,stu_name,tec_name):
        self.sch_name = sch_name
        A.__init__(self,stu_name)
        B.__init__(self,tec_name)
obj = C("DBS","Rohan","Madhu")
print("Student name is : ",obj.stu_name)
print("Teacher name is : ",obj.tec_name)
print("school name is : ",obj.sch_name)
