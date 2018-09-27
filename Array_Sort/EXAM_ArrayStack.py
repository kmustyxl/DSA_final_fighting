class ArrayStack:
    def __init__(self, arr_size):
        self.arr = []
        self.size = arr_size
    def push(self, data):
        if len(self.arr) < self.size:
            self.arr.append(data)
        else:
            raise Warning('Stack is full')
    def pop(self):
        if len(self.arr) >= 1:
            self.arr.pop()
        else:
            raise  Warning('Stack is empty')
Stack = ArrayStack(3)
Stack.push(1)
Stack.push(2)
print(Stack.arr)
Stack.pop()
print(Stack.arr)
