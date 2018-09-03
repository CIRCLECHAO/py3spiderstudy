class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_des(self):
        longname = str(self.year) + " " + self.make + ' ' + self.model
        return longname.title()


mynewcar = Car('audi', 'a4', 2019)
print(mynewcar.get_des())