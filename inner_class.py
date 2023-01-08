
# inner class

class car:
    def __init__(self):
        self.color = "red"
        self.type = "electric"
        self.obj2 = self.audi()

    def show_car(self):
        print(self.color)
        print(self.type)
    class audi:
        def __init__(self):
            self.model = "R8"
            self.year = 2010
        def show_audi(self):
            print(self.model)
            print(self.year)

obj = car()
obj.show_car()
obj.obj2.show_audi()