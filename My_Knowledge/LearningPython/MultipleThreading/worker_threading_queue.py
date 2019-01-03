import threading
from queue import Queue
import time

q = Queue()

num_worker_threads = 2

## Worker to get item/messages from queue and process it
def worker():
    while True:
        print("Waiting for Msg ..... {thread}\n".format(thread=threading.get_indent()))
        item = q.get()
        print("Message Received ..... {thread}---{msg}\n".format(msg=item, thread=threading.get_indent()))

        if item is None:
            q.task_done()
            break
        do_work(item)
        q.task_done()

#Function to process message
def do_work(item):
    print("Processing Message .... {thread}--{msg}\n".format(msg=item, thread=threading.get_indent()))
    time.sleep(2)
    print("Message Processed .... {thread}--{msg}\n".format(msg=item, thread=threading.get_indent()))

#Start Worker Threads
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# Add item to Queue
for item in ["AA", "BB", "CC"]:
    q.put(item)

# Stop all Workers
for i in range(num_worker_threads):
    q.put(None)

threading.enumerate()
