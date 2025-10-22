class Product:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    
    def sum(self,num3, num4):
        print(num3+num4)


product = Product(100,100)
product.sum(30,89)
# product.sum(10,30)
