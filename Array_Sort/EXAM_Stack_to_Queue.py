class StacktoQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, data):
        self.stack1.append(data)
    def pop(self):
        if len(self.stack2) == 0:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

queue = StacktoQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())