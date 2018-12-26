class queue:
    def __init__(self,queue_size):
        self.queue_size = queue_size
        self.begin = 0
        self.end = 0
        self.size = 0
        self.queue = [0 for i in range(self.queue_size)]
    def push(self,data):
        if self.size == self.queue_size:
            raise Warning('队列已满')
        else:
            self.queue[self.end] = data
            self.size += 1
            if self.end == self.queue_size-1:
                self.end = 0
            else:
                self.end += 1
    def pop(self):
        if self.size == 0:
            raise Warning('队列已空')
        else:
            return_num = self.queue[self.begin]
            self.size -= 1
            if self.begin == self.queue_size-1:
                self.begin = 0
            else:
                self.begin += 1
        return return_num

class Stack:
    def __init__(self,stack_size):
        self.queue = queue(stack_size)
        self.queue_help = queue(stack_size)
    def push(self,data):
        self.queue.push(data)
    def pop(self):
        while self.queue.size > 1:
            self.queue_help.push(self.queue.pop())
        return_num = self.queue.pop()
        tmp = self.queue
        self.queue = self.queue_help
        self.queue_help = tmp
        return return_num
a = Stack(3)
a.push(1)
a.push(2)
a.push(3)
print(a.pop())
print(a.pop())
print(a.pop())


