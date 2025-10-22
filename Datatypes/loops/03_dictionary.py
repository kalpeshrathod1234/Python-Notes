users = [
    {"id":10,"totalAmount":560,"coupon":"F10"},
    {"id":20,"totalAmount":789,"coupon":"S20"},
    {"id":30,"totalAmount":158,"coupon":"G30"}
]

coupons = {"F10": (0.2, 0), "S20":(0.5, 0), "G30":(0.1, 0)}


for user in users:
    percentage, amount = coupons.get(user["coupon"], (0, 0))
    discount = user["totalAmount"] * percentage + amount
    print(f"user id is {user["id"]} and total amount has to paid is {user["totalAmount"]} and they use coupon is {user["coupon"]} and they got discount is {discount}")