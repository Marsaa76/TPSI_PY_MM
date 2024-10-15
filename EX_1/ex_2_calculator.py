class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

num1 = 10
num2 = 5

sum_result = Calculator.add(num1, num2)
subtract_result = Calculator.subtract(num1, num2)
multiply_result = Calculator.multiply(num1, num2)
try:
    divide_result = Calculator.divide(num1, num2)
except ValueError as e:
    divide_result = str(e)

print(f"Addition: {num1} + {num2} = {sum_result}")
print(f"Subtraction: {num1} - {num2} = {subtract_result}")
print(f"Multiplication: {num1} * {num2} = {multiply_result}")
print(f"Division: {num1} / {num2} = {divide_result}")