class student:
    def __init__(self,stu_name,stu_age,stu_marks,stu_contact):
        self.stu_name = stu_name
        self.stu_age = stu_name
        self.stu_marks = stu_marks
        self.stu_contact = stu_contact

class employee(student):
    def __init__(self,emp_id,emp_name,emp_designation,emp_salary,stu_name,stu_age,stu_marks,stu_contact):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_designation = emp_designation
        self.emp_salary = emp_salary
        super().__init__(stu_name,stu_age,stu_marks,stu_contact)

obj = employee(101,"Sagar","Officer",20000,"Kiran",23,459,1365487912)

print("Employee name is : ", obj.emp_name)
print("Employee id is : ", obj.emp_id)
print("Student name is : ", obj.stu_name)
print("Student contact is : ", obj.stu_contact)