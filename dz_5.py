class car:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.brand = "BMW"
        self.price = "500000$"


class machine:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = "Electric"


class vehicle:
    pass


class BMW(car, machine, vehicle):
    def car_info(self):
        print(f"\nCar info(BMW X10): \n\tBrand - {self.brand};\n\tPrice - {self.price};\n\tEngine - {self.engine}.")


BMW_X10 = BMW()
BMW_X10.car_info()
