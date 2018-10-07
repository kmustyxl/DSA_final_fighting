def upstairs_recur(n):
    '''
    递归版
    :param n:
    :return:
    '''
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return upstairs_recur(n-1) + upstairs_recur(n-2)

def upstairs_unrecur(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        a = 1
        b = 2
        for i in range(3, n+1):
            temp = a+b
            a = b
            b = temp
    return b
ans = upstairs_unrecur(60)
print(ans)
