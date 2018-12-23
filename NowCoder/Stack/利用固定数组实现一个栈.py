'''
定义一个大小范围固定的栈
利用一个指针index去确定栈顶的实时位置
'''
class Stack:
    def __init__(self,stack_size):
        self.stack_size = stack_size
        self.stack = [0 for i in range(stack_size)]
        self.stack_index = -1
    def push(self,data):
        if self.stack_index <= self.stack_size - 1:
            self.stack_index += 1
            self.stack[self.stack_index] = data
        else:
            raise Warning('栈已满')
    def pop(self):
        if self.stack_index >= 0:
            re_num = self.stack[self.stack_index]
            self.stack[self.stack_index] = 0
            self.stack_index -= 1
            return re_num
        else:
            raise Warning('栈已空')

