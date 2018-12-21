def getmax(arr,l,r):
    '''
    功能：寻找数组中的最大值
    tips：先找数组中左部分最大值，再找右部分最大值，最后求得数组最大值，分治思想。
    递归行为的实质：系统自动将函数入栈
    每次执行子调用就入栈（所有当前参数的信息及程序运行行数情况），执行return就出栈（系统复原出栈的所有参数信息，继续往下执行），
    *并*将return结果返回给此时弹出的leftmax或者rightmax；
    '''
    if l == r:          #递归基：实质为函数出栈的条件
        return arr[l]
    mid = l + int((r-l)/2)
    leftmax = getmax(arr,l,mid) #leftmax为调用的子过程的返回值
    rightmax = getmax(arr,mid+1,r)
    return max(leftmax,rightmax)

if __name__ == "__main__":
    arr = [5,6,2,9]
    ans = getmax(arr,0,len(arr)-1)
    print(ans)
