def printmatrix(matrix):
    '''
    循环打印矩阵，eg：
    1 2 3
    4 5 6
    7 8 9
    要求打印顺序为：1-2-3-6-9-8-7-4-5
    tip：
    跳出矩阵的限制，从宏观角度看这个问题，循环打印矩阵，先打印最外层一圈，按照此逻辑再打印内层的一圈
    需要处理的边界问题：
       1. 矩阵只有一行
       2. 矩阵只有一列
    '''
    if matrix is None:
        return
    l1 = 0    #矩阵左顶点坐标（l1,l2）
    l2 = 0
    r1 = len(matrix) - 1    #矩阵右顶点坐标（r1,r2）
    r2 = len(matrix[0]) - 1
    while l1 <= r1 and l2 <= r2:
        l1,l2,r1,r2 = printedge(matrix,l1,l2,r1,r2)
    return

def printedge(matrix,l1,l2,r1,r2):
    cur1 = l1
    cur2 = l2    #(cur1,cur2)为当前需要打印的坐标
    if l1 == r1:    #第一种边界问题
        for i in range(cur2,r2+1):
            print(matrix[cur1][i])
    elif l2 == r2:    #第二种边界问题
        for i in range(cur1,r1+1):
            print(matrix[i][cur2])
    else:
        while cur2 < r2:
            print(matrix[cur1][cur2])
            cur2 += 1
        while cur1 < r1:
            print(matrix[cur1][cur2])
            cur1 += 1
        while cur2 > l2:
            print(matrix[cur1][cur2])
            cur2 -= 1
        while cur1 > l1:
            print(matrix[cur1][cur2])
            cur1 -= 1
    l1 += 1
    l2 += 1
    r1 -= 1
    r2 -= 1
    return l1,l2,r1,r2
if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    printmatrix(matrix)


