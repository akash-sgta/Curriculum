class Queue(object):

    def __init__(self, typeof='class', size=10):
        self.typeof = typeof
        self._size = size
        self._array = [0 for i in range(self.size)]
        self._shape = 0
        self.front = -1
        self.rear = -1

    @property
    def array(self):
        return self._array

    @property
    def size(self):
        return self._size

    @property
    def shape(self):
        return self._shape
    
    @shape.setter
    def shape(self, data):
        self._shape = data

    def enqueue(self):
        pass
    def dequeue(self):
        pass

    def __str__(self):
        queue_ = ""
        for i in range(0, self.size):
            queue_ += f'[{self.array[i]}] '
        return queue_

class Linear_Queue(Queue):

    def __init__(self, typeof='class', size=10):
        super().__init__(typeof, size)

    def enqueue(self, data):
        if (self.front == 0 and self.rear == self.size-1) or (self.front == self.rear + 1):
            return False,"Overflow"
        else:
            if self.typeof in str(type(data)):
                if self.front == -1:
                    self.front, self.rear = 0,0
                elif self.rear == self.size-1:
                    self.rear = 0
                else:
                    self.rear += 1
                self.array[self.rear] = data
                self.shape += 1
                return True,data
            else:
                return False,"Invalid DataType"

    def dequeue(self):
        if self.front == -1:
            return False,"UnderFlow"
        else:
            data = self.array[self.front]
            self.array[self.front] = None
            self.shape -= 1
            if self.front == self.rear:
                self.front, self.rear = -1, -1
            elif self.front == self.size-1:
                self.front = 0
            else:
                self.front += 1
            return True,data


class Circular_Queue(Queue):

    def __init__(self, typeof='class', size=10):
        super().__init__(typeof, size)

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            return False,"Overflow"
        else:
            if self.typeof in str(type(data)):
                if self.front == -1:
                    self.rear,self.front = 0,0
                else:
                    self.rear = (self.rear + 1) % self.size
                self.array[self.rear] = data
                self.shape += 1
                return True,data
            else:
                return False,"Invalid DataType"

    def dequeue(self):
        if self.front == -1:
            return False,"UnderFlow"
        else:
            data = self._array[self.front]
            self.shape -= 1
            self.array[self.front] = None
            if self.front == self.rear:
                self.front, self.rear = -1, -1
            else:
                self.front = (self.front + 1) % self.size
            return True,data


class Doubly_Ended_Queue(Queue):

    def __init__(self, typeof='class', size=10):
        super().__init__(typeof, size)

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            return False,"Overflow"
        else:
            if self.typeof in str(type(data)):
                if self.front == -1:
                    self.rear,self.front = 0,0
                else:
                    self.rear = (self.rear + 1) % self.size
                self._array[self.rear] = data
                return True,data
            else:
                return False,"Invalid DataType"

    def dequeue(self):
        if self.front == -1:
            return False,"UnderFlow"
        else:
            data = self._array[self_.front]
            self._array[self.front] = None
            if self.front == self.rear:
                self.front, self.rear = -1, -1
            else:
                self.front = (self.front + 1) % self.size
            return True,data

def main():

    stack = Linear_Queue('int', 5)
    # stack = Circular_Queue('int', 5)
    print(stack.size)
    print(str(stack))
    print(stack.enqueue(10))
    print(stack.enqueue(20))
    print(str(stack))
    print(stack.enqueue(30))
    print(stack.enqueue(40))
    print(str(stack))
    print(stack.dequeue())
    print(stack.dequeue())
    print(str(stack))
    print(stack.enqueue(50))
    print(stack.enqueue(60))
    print(str(stack))
    print(stack.enqueue(70))
    print(stack.enqueue(80))
    print(str(stack))
    print(stack.enqueue(90))
    print(stack.enqueue(100))
    print(str(stack))
    print(stack.enqueue(200))
    print(stack.enqueue(300))
    print(str(stack))
    print(stack.enqueue(400))
    print(stack.dequeue())
    print(str(stack))
    print(stack.dequeue())
    print(stack.dequeue())
    print(str(stack))
    print(stack.dequeue())
    print(stack.dequeue())
    print(str(stack))
    print(stack.enqueue(30))
    print(stack.enqueue(40))
    print(str(stack))
    print(stack.enqueue(50))
    print(stack.enqueue(60))
    print(str(stack))
    print(stack.enqueue(70))
    print(stack.dequeue())
    print(str(stack))
    print(stack.dequeue())
    print(stack.dequeue())
    print(str(stack))
    print(stack.dequeue())
    print(stack.dequeue())
    print(str(stack))
    print(stack.dequeue())
    print(stack.dequeue())
    print(str(stack))

# main()
#----Documentation----
'''
    returns True/False depending on success followed by desired output or error message
'''