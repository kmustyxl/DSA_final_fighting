'''
需要引入三个变量 start（队列返回的指针）
               end（队列插入数值的指针）
               size（当前队列规模）tips：引入size可以有效地将start与end进行解耦，使得
                                       start与end分别和size有关系，而它两者本身不产生关系，
                                       便于理解逻辑与写代码。
'''
class Queue:
    def __init__(self,Queue_size):
        self.start = 0
        self.end = 0
        self.size = 0
        self.queue_size = Queue_size
        self.queue = [0 for i in range(Queue_size)]
    def push(self,data):
        if self.size >= self.queue_size:
            raise Warning('队列已满')
        else:
            self.queue[self.end] = data
            self.size += 1
            if self.end == self.queue_size - 1:  #判断end指针是否触底
                self.end = 0
            else:
                self.end += 1
    def pop(self):
        if self.size == 0:
            raise Warning('队列已空')
        else:
            re_num = self.queue[self.start]
            if self.start == self.queue_size - 1:  #判断start指针是否触底
                self.start = 0
            else:
                self.start += 1
            self.size -= 1
        return re_num



