
class car:

    def __init__(self,color, engine_in_cc, seates_no):
        self.color = color
        self.engine_in_cc = engine_in_cc
        self.seates_no = seates_no

    def print_car_details(self):
        print(f"your car color is {self.color} and you car is {self.engine_in_cc}CC engine and this car is {self.seates_no} seater")


class mercedes(car):

    car1 = car("black and red","2500",5)

    print(car1.print_car_details())


class bmw(car):

    car2 = car

    def __init__(self):
        pass

    def car_details(self):
        self.car2(color="red",seates_no=6, engine_in_cc=2500)
        self.print_car_details(self.car2)