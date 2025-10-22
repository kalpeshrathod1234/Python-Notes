class car:

    def __init__(self):
        print(f"car class constructor call")
    
    def say_hi(self):
        print(f"hi from car class")

class bmw(car):

    def print_car(self):
        print()
        super().__init__()
        super().say_hi()
    

carss = bmw()
carss.print_car()
