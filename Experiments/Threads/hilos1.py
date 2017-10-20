import time
from threading import Thread

def sleeper(i):
    print("thread {} sleeps for 5 seconds".format(i) )
    time.sleep(10)
    print("thread {} woke up".format(i))

for i in range(100):
    t = Thread(target=sleeper, args=(i,))
    t.start()