import asyncio

async def calculate_factorial(number):
   #Calculates the factorial of a number asynchronously.
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
        await asyncio.sleep(0)  # Yield control to the event loop
    return result

async def display_factorials(numbers):
    #Calculates and displays factorials asynchronously for a list of numbers.
    tasks = [asyncio.create_task(calculate_factorial(num)) for num in numbers]  # Create tasks
    results = await asyncio.gather(*tasks)  # Gather results from all tasks
    
    for num, res in zip(numbers, results):  # Display results
        print(f"Factorial of {num} is {res}")

async def main():
    #Main function to calculate factorials asynchronously.
    numbers = [5, 7, 10]  # Numbers for factorial calculation
    print("Starting asynchronous factorial calculations...")
    await display_factorials(numbers)
    print("All calculations completed.")

if __name__ == "__main__":
    asyncio.run(main())  # Execute the main async function
