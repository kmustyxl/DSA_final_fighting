class ArrayQueue:
    '''
    定义两个指针，Start表示pop()的数据地址，End表示push()的地址，执行一次push，cur_size+1
    执行一次pop(),cur_size-1.
    当Start触底时，重新置零，End同理。
    '''
    def __init__(self, size_arr):
        self.arr = [0 for i in range(size_arr)]
        self.size = size_arr
        self.start = 0
        self.end = 0
        self.cur_size = 0
    def push(self, data):
        if self.cur_size < self.size:
            self.arr[self.end] = data
            self.end += 1
            self.cur_size += 1
            if self.end == self.size: #end触底
                self.end = 0
        else:
            raise Warning('Queue is full')
    def pop(self):
        if self.cur_size > 0:
            tmp = self.start
            self.start += 1
            self.cur_size -= 1
            if self.start == self.size: #start触底
                self.start = 0
            return self.arr[tmp]
        else:
            raise Warning('Queue is empty')

Queue = ArrayQueue(3)
Queue.push(1)
Queue.push(2)
Queue.push(3)
ans = Queue.pop()
print(ans)
Queue.push(4)
ans = Queue.pop()
print(ans)
ans = Queue.pop()
print(ans)
ans = Queue.pop()
print(ans)


