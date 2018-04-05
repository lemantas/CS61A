from queue import Queue
import threading

queue = Queue()

# Syncronized versions of consumer and producer
def synchronized_consume():
    while True:
        print('Got an item:', queue.get())
        queue.task_done()

# A function becomes a Daemon ^^ True story, dude     
def synchronized_produce():
    consumer = threading.Thread(target=synchronized_consume, args=())
    consumer.daemon = True
    consumer.start()
    for i in range(10):
        queue.put(i)
    queue.join()
    
synchronized_produce()
