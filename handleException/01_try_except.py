chai_menu = {"mint chai": 60, "masala chai": 20}

try:
    a = 20/0
    chai_menu["gainger"]
except KeyError:
    print("key is not found")
except ZeroDivisionError:
    print("value is not divide zero")

    
print("hi bro")