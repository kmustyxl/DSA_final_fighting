class stack:
    '''
    题目：实现一个栈，并返回当前栈中的最小元素

    本题需要两个栈，一个是随数据正常压栈的stack1，另一个是辅助栈stack2.在压入数据时，如果stack1的栈顶大于stack2栈顶，
    则，stack2重复压入当前栈顶，如果stack1栈顶小于stack2栈顶，则stack2压入stack1栈顶数据。
    '''
    def __init__(self):
        self.arr = []
    def push(self,data):
        self.arr.append(data)
        return self.arr
    def pop(self):
        self.arr.pop()
        return self.arr
    def stack_top(self):
        return self.arr[-1]
def Stack_min_number(arr, stack1, stack2):
    stack1.push(arr[0])
    stack2.push(arr[0])
    for i in range(1, len(arr)):
        stack1.push(arr[i])
        if stack1.stack_top() >= stack2.stack_top():
            stack2.push(stack2.stack_top())
        else:
            stack2.push(arr[i])
    return stack2.stack_top()

arr = [4,2,3,4,6]
stack1 = stack()
stack2 = stack()
ans = Stack_min_number(arr, stack1, stack2)
print(ans)
