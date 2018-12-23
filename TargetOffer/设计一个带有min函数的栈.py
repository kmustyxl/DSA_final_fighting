'''
要求一：栈的push、pop、min函数时间复杂度为1
要求二：随时可以获取当前栈中的最小数值
-----------------------------------------
tips：
借助一个同等规模的辅助栈，伴随着主栈的push和pop操作，辅助栈同步执行
辅助栈push操作：
             如果主栈push的数值大于等于辅助栈栈顶，则将辅助栈栈顶数值进行一次复制
             如果主栈push的数值小于辅助栈栈顶，则将该数值同样压入辅助栈中
'''
class Stack_with_min:
    def __init__(self,stack_size):
        self.stack_size = stack_size
        self.stack_A = [0 for i in range(stack_size)]
        self.stack_B = [0 for i in range(stack_size)]
        self.stack_index = -1
    def push(self,data):
        if self.stack_index <= self.stack_size - 1:
            self.stack_index += 1
            self.stack_A[self.stack_index] = data
            if self.stack_index == 0:                     #辅助栈
                self.stack_B[self.stack_index] = data
            else:
                push_data_B = min(data,self.stack_B[self.stack_index-1])
                self.stack_B[self.stack_index] = push_data_B
        else:
            raise Warning('栈已满')
    def pop(self):
        if self.stack_index >= 0:
            re_num = self.stack_A[self.stack_index]
            self.stack_A[self.stack_index] = 0
            self.stack_index -= 1
            return re_num
        else:
            raise Warning('栈已空')
    def min(self):
        return self.stack_B[self.stack_index]
a = Stack_with_min(4)
a.push(4)
a.push(2)
a.push(5)
a.push(1)
print(a.min())
a.pop()
print(a.min())

