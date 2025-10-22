
class car:

    @staticmethod
    def print_car_info(text):
        return [item.strip() for item in text.split(",")]
    

bmw = "bmw,  1250cc  , white  ,                 black"
car1 = car.print_car_info(bmw)
print(car1)