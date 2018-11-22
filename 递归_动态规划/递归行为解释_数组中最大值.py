def getmax(arr,l,r):
    '''
    功能：寻找数组中的最大值
    tips：先找数组中左部分最大值，再找右部分最大值，最后求得数组最大值，分治思想。
    递归行为的实质：系统自动将函数入栈
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
    # 0 初始为getmax(arr,0,3);mid=1
    # 1 执行到第十行，系统将getmax(arr,0,3);mid=1;当前为第十行程序。。等所有信息入栈，然后
    # 2 进行子调用，此时为getmax(arr,0,1);mid=0;当前为第十行程序。。继续入栈；然后
    # 3 进行子调用，此时满足递归基条件，系统之前的所有操作均在栈里，系统执行出栈，恢复现场，函数接着从第十行往后
    #   继续执行，并将arr[0]=5 返回给leftmax；
    # 4 执行第十一行，系统将getmax(arr,0,1);mid=0;当前为第十一行程序，leftmax=5。。入栈；然后执行子调用
    # 5 此时，