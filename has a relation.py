
# is a relation - inheritance

# has a relation - indirectly accessing other classes data

#                  one class object behaves as a data member of another class

class car:
    def __init__(self,color,type):
        self.color = color
        self.type = type

    def show_car(self):
        print(self.color)
        print(self.type)
class audi:
    def __init__(self,model,year,car1):
        self.model = "R8"
        self.year = 2010
        self.car = car1
    def show_audi(self):
        print(self.model)
        print(self.year)

a = car("red","electric")
b = audi("R8",2010,a)

b.show_audi()
print(b.car.color)
b.car.show_car()