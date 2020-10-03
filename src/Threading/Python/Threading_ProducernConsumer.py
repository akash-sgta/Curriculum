import threading
import time
import random

BUF_SIZE = 10
q = []

class ProducerThread(threading.Thread):
    def __init__(self, target=None, name=None):
        super().__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if 0< len(q) <11:
                item = random.randint(1,10)
                q.put(item)
                print('Putting '
                	+str(item)
                	+' : '
                	+str(q.qsize())
                	+' items in queue')
                time.sleep(random.random())
        return

class ConsumerThread(threading.Thread):
    def __init__(self, target=None, name=None):
        super().__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if len(q) != 0:
                item = q.get()
                print('Getting '
                	+str(item)
                	+' : '
                	+str(q.qsize())
                	+' items in queue')
                time.sleep(random.random())
        return

if __name__ == '__main__':
    
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)