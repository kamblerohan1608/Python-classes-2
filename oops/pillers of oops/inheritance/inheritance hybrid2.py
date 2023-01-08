class company:
    def __init__(self,req):
        self.req = req

class developer(company):
    def __init__(self,dev_req,req):
        self.dev_req = dev_req
        super().__init__(req)

class tester(company):
    def __init__(self,test_req,dev_req,req):
        self.test_req = test_req
        super().__init__(dev_req,req)
        
class project(developer,tester):
    def __init__(self,pro_name,test_req,dev_req,req):
        self.pro_name = pro_name
        super().__init__(test_req,dev_req,req)

def main():
    obj = project("abc.com",5,10,15)

    print("company requirement : ",obj.req)
    print("developer requirement : ",obj.dev_req)
    print("tester requirement : ",obj.test_req)
    print("project name : ",obj.pro_name)

main()