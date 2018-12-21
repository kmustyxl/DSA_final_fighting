class Queue:
    def __init__(self,size):
        self.arr = [-1 for i in range(size)]
        self.start = 0
        self.end = 0
        self.cursize = 0
        self.size = size
    def push(self, data):
        if self.cursize < self.size:
            self.arr[self.end] = data
            self.end += 1
            self.cursize += 1
            if self.end == self.size:
                self.end = 0
        else:
            raise Warning('Queue is full')
    def pop(self):
        if self.cursize > 0:
            tmp = self.start
            self.start += 1
            self.cursize -=1
            if self.start == self.size:
                self.start = 0
            return self.arr[tmp]
        else:
            raise Warning('Queue is empty')

def swap(q1, q2):
    return q2, q1

class QueuetoStack:
    def __init__(self,size):
        self.queue1 = Queue(size)
        self.queue2 = Queue(size)
    def push(self, data):
        self.queue1.push(data)
    def pop(self):
        if self.queue1.cursize < 1:
            raise Warning('Stack is empty')
        else:
            while self.queue1.cursize > 1:
                self.queue2.push(self.queue1.pop())
            ans = self.queue1.pop()
            self.queue1, self.queue2 = swap(self.queue1, self.queue2)
        return ans

QUEUE = QueuetoStack(4)
QUEUE.push(1)
QUEUE.push(2)
QUEUE.push(3)
QUEUE.push(4)
print(QUEUE.pop())
print(QUEUE.pop())
print(QUEUE.pop())
print(QUEUE.pop())