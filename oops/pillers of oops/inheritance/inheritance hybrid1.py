#1
'''
class company:
    def m1(self):
        self.req=20
class developer(company):
    def m2(self):
        self.dev_count = 10
class tester(company):
    def m3(self):
        self.test_count = 8
class project(developer,tester):
    def m4(self):
        self.pro_name = "abc project"

def main():
    obj = project()
    obj.m1()
    obj.m2()
    obj.m3()
    obj.m4()

    print("company requirement ",obj.req)
    print("developer requirement ",obj.dev_count)
    print("tester requirement ",obj.test_count)
    print("project name ",obj.pro_name)

main()
'''
#with constructor

class company:
    def __init__(self):
        self.req = 20
class developer(company):
    def __init__(self):
        self.dev_count = 10
        super().__init__()
class tester(company):
    def __init__(self):
        self.test_count = 8
        super().__init__()
class project(developer,tester):
    def __init__(self):
        self.pro_name = "abc project"
        developer.__init__(self)
        tester.__init__(self)

def main():
    obj = project()

    print("company requirement ",obj.req)
    print("developer requirement ",obj.dev_count)
    print("tester requirement ",obj.test_count)
    print("project name ",obj.pro_name)

main()