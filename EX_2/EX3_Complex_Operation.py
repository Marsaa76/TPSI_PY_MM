import threading
import time

def perform_calculation():
    result = sum(range(1, 1000001))  # Perform the calculation
    print(f"Calculation complete. Result: {result}")
    perform_calculation_complete.set()  # Signal that the calculation is done

def show_status():
    while not perform_calculation_complete.is_set():  # Check if calculation is complete
        print("Calculation in progress...")
        time.sleep(0.5)  # Pause for 500 milliseconds

# Create an event to indicate completion of the calculation
perform_calculation_complete = threading.Event()

# Create and start the threads
calculation_thread = threading.Thread(target=perform_calculation)
status_thread = threading.Thread(target=show_status)

calculation_thread.start()
status_thread.start()

# Wait for the calculation thread to complete
calculation_thread.join()

# Wait for the status thread to finish
status_thread.join()
