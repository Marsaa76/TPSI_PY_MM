import threading

counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(1000):
        with counter_lock:
            counter += 1

threads = [threading.Thread(target=increment_counter) for _ in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
