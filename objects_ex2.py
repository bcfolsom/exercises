class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print('{} {} {}'.format(self.year, self.make, self.model))

car = Vehicle('Subaru', 'Forester', 2010)
print(car.make, car.model, car.year)
car.print_info()
