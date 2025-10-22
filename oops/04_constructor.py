class car:

    def __init__(self,color, engine_in_cc):
        self.color = color
        self.engine_in_cc = engine_in_cc
    
    def print_car(self):
        return f"your car color is {self.color} and your engine is {self.engine_in_cc} CC"
    

bmw = car("white","2000")
print(bmw.print_car())
mahindra = car("black","1500")
print(mahindra.print_car())