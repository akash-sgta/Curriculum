import threading
import time
import random

product = 0
condition = threading.Lock() # for critical section
quanta = 1

class Producer(threading.Thread):

    def __init__(self, val='Thread'):
        self._name = val
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = str(val)
    
    def run(self):
        global product
        count = time.time()
        while time.time()-count < quanta:
            f = random.randrange(1, 5)
            condition.acquire()
            product = product + f
            time.sleep(random.random()/10)
            print(f"{self.name} : Add-{f}     | Stock-{product}")
            condition.release()

class Consumer(threading.Thread):

    def __init__(self, val='Thread'):
        self._name = val
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = str(val)

    def run(self):
        global product
        count = time.time()
        while time.time()-count < quanta:
            f = random.randrange(5, 10)
            condition.acquire()
            if f >= product:
                print(f"{self.name} : Require-{f} | Stock-{product} | Get-{product} | Starve-{f-product}")
                product = 0
            else:
                print(f"{self.name} : Require-{f} | Stock-{product} | Get-{f} | Starve-0")
                product = product - f
            time.sleep(random.random()/10)
            condition.release()
                
def main():
    global product
    product = 0
    print(f"Product : {product}")
    producer_ref = Producer('P')
    consumer_ref = Consumer('C')
    producer_thread = threading.Thread(target=producer_ref.run, args=())
    consumer_thread = threading.Thread(target=consumer_ref.run, args=())

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print(f"Product : {product}")

main()