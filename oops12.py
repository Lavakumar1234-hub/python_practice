class Product:
    tax_rate=5
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        return self.base_price+(self.base_price*(Product.tax_rate/100))
    @classmethod
    def change_tax_rate(cls,new_rate):
        cls.tax_rate=new_rate
    @staticmethod
    def is_valid_price(price):
        return 0<=price<=100000
    def display(self):
        print("NAME:",self.name)
        print("BASE PRICE:",self.base_price)
        print("FINAL PRICE:",self.final_price())
        print("VALID PRICE:",Product.is_valid_price(self.base_price))
        print()
s1=Product("LAPTOP",50000)
s2=Product("KEYBOARD",2000)
s3=Product("MOUSE",-500)
products=[s1,s2,s3]
print("BEFORE CHANGING TAX RATE:")
for product in products:
    product.display()
Product.change_tax_rate(10)
print("AFTER CHANGING TAX RATE to 10%:")
for product in products:
    product.display()
