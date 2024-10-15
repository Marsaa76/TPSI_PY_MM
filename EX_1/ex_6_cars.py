class Car:
    total_cars = 0

    def __init__(self, model, brand, year, price):
        self.model = model
        self.brand = brand
        self.year = year
        self.price = price
        Car.total_cars += 1

    def display_details(self):
        return (f"Model: {self.model}\n"
                f"Brand: {self.brand}\n"
                f"Year: {self.year}\n"
                f"Price: €{self.price}")

    def calculate_depreciation(self):
        current_year = Car.get_current_year()
        age = current_year - self.year
        depreciation_value = self.price * 0.15 * age
        current_value = self.price - depreciation_value
        return max(current_value, 0)

    @staticmethod
    def get_total_cars():
        return Car.total_cars

    @staticmethod
    def get_current_year():
        return 2024  # You can change this value or implement logic to fetch the real current year

    @classmethod
    def compare_cars(cls, car1, car2):
        if car1.price > car2.price:
            return f"{car1.brand} {car1.model} is more expensive."
        elif car1.price < car2.price:
            return f"{car2.brand} {car2.model} is more expensive."
        else:
            return "Both cars have the same price."

car1 = Car("Model S", "Tesla", 2020, 80000)
car2 = Car("Civic", "Honda", 2018, 22000)

print(car1.display_details())
print()
print(car2.display_details())
print()
print(f"Current value of {car1.model} after depreciation: €{car1.calculate_depreciation()}")
print(f"Current value of {car2.model} after depreciation: €{car2.calculate_depreciation()}")
print()
print(f"Total number of cars created: {Car.get_total_cars()}")
print(Car.compare_cars(car1, car2))