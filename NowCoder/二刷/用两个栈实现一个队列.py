class Stack:
    def __init__(self,stack_size):
        self.stack = [0 for i in range(stack_size)]
        self.stack_size = stack_size
        self.index = 0
        self.size = 0
    def push(self,data):
        if self.size == self.stack_size:
            raise Warning('栈已满')
        else:
            self.stack[self.index] = data
            self.size += 1
            self.index += 1
    def pop(self):
        if self.size == 0:
            raise Warning('栈已空')
        else:
            return_num = self.stack[self.index-1]
            self.index -= 1
            self.size -= 1
        return return_num

class Queue:
    def __init__(self,queue_size):
        self.stack = Stack(queue_size)
        self.stack_help = Stack(queue_size)
    def push(self,data):
        self.stack.push(data)
    def pop(self):
        if self.stack_help.size > 0:
            return_num = self.stack_help.pop()
        else:
            while self.stack.size > 0:
                self.stack_help.push(self.stack.pop())
            return_num = self.stack_help.pop()
        return return_num

a = Queue(5)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print(a.pop())
print(a.pop())
a.push(6)
print(a.pop())
