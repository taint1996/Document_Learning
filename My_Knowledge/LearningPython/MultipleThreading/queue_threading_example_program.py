from queue import Queue
import time
from threading import Thread, Lock

print_lock = Lock()

def exampleJob(worker):
    time.sleep(0.5)

    with print_lock:
        print(Thread.name, worker)

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

q = Queue()

for x in range(10):
    #start Thread
    t = Thread(target=threader)
    t.setDaemon(True)
    t.start()

start_time = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print("It tooks: ", str(time.time() - start_time) + " seconds")
