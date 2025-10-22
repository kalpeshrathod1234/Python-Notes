class bike:

    def __init__(self,bike_color, bike_break, bike_price):
        self.bike_color = bike_color
        self.bike_break = bike_break
        self.bike_price = bike_price

    @classmethod
    def get_dict(cls, bike_info):
        return cls(
            bike_info["bike_color"],
            bike_info["bike_break"],
            bike_info["bike_price"]
        )
    
    def print_bike_info(self):
        print(f"your bike color is {self.bike_color} and your bike have {self.bike_break} break and bike price is {self.bike_price} RS")

    


tvs_rider = bike("red","disk",95000)
tvs_rider.print_bike_info()

info_dect = {"bike_price":89642,"bike_color":"black","bike_break":"drum"}
appache = bike.get_dict(info_dect)
appache.print_bike_info()