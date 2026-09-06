from multiprocessing import Process
import threading


#==================================
# Multiprocessing
#==================================
# Multiprocessing creates multiple processes. Each process has its own Python interpreter and memory space.
"""
def task():
    print("Running task")

p1 = Process(target=task)
p2 = Process(target=task)

p1.start()
p2.start()

p1.join()
p2.join()
"""

#=============================
## Multithreading
# Multithreading creates multiple threads inside the same process.
#=============================
def task():
    print("Threading task")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

