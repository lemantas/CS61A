import threading
from time import sleep


counter = [0]

def increment():
    count = counter[0]
    sleep(0)
    counter[0] = count + 1
    
other = threading.Thread(target=increment, args=())
other.start()
increment()

# The count will vary between 1 and 2, because different threads 
# simultaneously access mutable variable counter
print('count is now: ', counter[0])
