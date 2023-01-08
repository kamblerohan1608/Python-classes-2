class student:
    def __init__(self,stu_name,stu_age,stu_loc):
        self.stu_name = stu_name
        self.stu_age = stu_age
        self.stu_loc = stu_loc

class employ(student):
    def __init__(self,emp_name,emp_salary,emp_contact,stu_name,std_age,stu_loc):
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_contact = emp_contact
        super().__init__(stu_name,std_age,stu_loc)
    
class company(employ):
    def __init__(self,com_name,com_location,com_branch,emp_name,emp_salary,emp_contact,stu_name,std_age,stu_loc):
        self.com_name = com_name
        self.com_location = com_location
        self.com_brance = com_branch
        
        super().__init__(emp_name,emp_salary,emp_contact,stu_name,std_age,stu_loc)

obj = company("tata",)
print("Enter company name : ", obj.com_name)
print("Enter employee name : ", obj.emp_name)
print("Enter student name : ", obj.stu_name)