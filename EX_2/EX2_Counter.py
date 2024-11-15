import threading
sem = threading.Semaphore(0)

def count_up():
    for i in range(1, 11):
        print(f"Counting up: {i}")
        sem.release()

def count_down():
    sem.acquire()
    for i in range(10, 0, -1):
        print(f"Counting down: {i}")


up_thread = threading.Thread(target=count_up)
down_thread = threading.Thread(target=count_down)

up_thread.start()
down_thread.start()

up_thread.join()
down_thread.join()
