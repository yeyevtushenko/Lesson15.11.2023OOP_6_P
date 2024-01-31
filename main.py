class Wheels:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def display_info(self):
        print(f"Wheels: Brand - {self.brand}, Size - {self.size}")


class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def display_info(self):
        print(f"Engine: Fuel Type - {self.fuel_type}, Horsepower - {self.horsepower}")


class Doors:
    def __init__(self, number, style):
        self.number = number
        self.style = style

    def display_info(self):
        print(f"Doors: Number - {self.number}, Style - {self.style}")


class Car(Wheels, Engine, Doors):
    def __init__(self, brand, size, fuel_type, horsepower, number_of_doors, door_style):
        Wheels.__init__(self, brand, size)
        Engine.__init__(self, fuel_type, horsepower)
        Doors.__init__(self, number_of_doors, door_style)

    def display_car_info(self):
        print("Car Information:")
        super().display_info()
        Engine.display_info(self)
        Doors.display_info(self)


my_car = Car(brand="Michelin", size=17, fuel_type="Diesel", horsepower=130, number_of_doors=3, door_style="Coupe")
my_car.display_car_info()

