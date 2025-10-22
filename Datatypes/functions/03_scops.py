
# def chai_order():
#     chai_type = "masala"  # enclosing scop
#     def order_chai():
#         chai_type = "mint" # local scope
#         print(f"inner def {chai_type} chai")
#     order_chai()
#     print(f"outer def {chai_type} chai")


# chai_type = "normal" # global scope
# chai_order()
# print(f"global {chai_type} chai")




def order_chai():
    chai_type = "ginger"
    def kitchen():
        nonlocal chai_type
        chai_type = "kaser"
    kitchen()
    print(f"chai type is: {chai_type}")

order_chai()

