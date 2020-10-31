from threading import *
from time import sleep

def test1():
    for _ in range(5):
        print("hi, this is first thread")
        sleep(2)
def test2():
    for _ in range(5):
        print("hi, this is second thread")
        sleep(2)

t1 = Thread(target=test1)
t2 = Thread(target=test2)

t1.start()
sleep(0.2)
t2.start()