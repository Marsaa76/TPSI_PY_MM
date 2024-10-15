class Product:
    total_products = 0

    def __init__(self, name, quantity, price):
        
        self.name = name
        self.quantity = quantity
        self.price = price
        

        Product.total_products += 1


    def calculate_total_value(self):
        return self.quantity * self.price

    @staticmethod
    def get_total_products():
        return Product.total_products

product1 = Product("Laptop", 10, 1200)
product2 = Product("Smartphone", 25, 600)

# Calculate the total value of products 
print(f"Total value of {product1.name}: ${product1.calculate_total_value()}")
print(f"Total value of {product2.name}: ${product2.calculate_total_value()}")

print(f"Total products created: {Product.get_total_products()}")