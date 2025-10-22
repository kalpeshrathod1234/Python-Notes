class chai:
    chai_type = "normal"
    chai_cups = 10

order = chai()
order.chai_type = "ginger"
order.chai_cups = 2

del order.chai_type
print(order.chai_type)
order.chai_size = "medium"
del order.chai_size
print(order.chai_size)