'''
将一个正方形数组矩阵顺时针旋转90度
tips：
     从外层，一层一层旋转，只需搞定最外层即可同理
'''
import sys
def read_input():
    try:
        input_martix = []
        while True:
            line = sys.stdin.readline().strip()
            if line == '':
                break
            input_martix.append(list(map(int,line.split())))
    except:
        pass
    return input_martix
def rotate(matrix):
    l1 = 0
    l2 = 0
    r1 = len(matrix) - 1
    r2 = len(matrix[0]) - 1
    while l1 < r1:
        rotateedge(matrix,l1,l2,r1,r2)
        l1 += 1
        l2 += 1
        r1 -= 1
        r2 -= 1
    return matrix
def rotateedge(matrix,l1,l2,r1,r2):
    len_edge = r1 - l1
    for i in range(len_edge):
        tmp = matrix[l1][l2+i]  #想着各自的位置将由哪个位置的数字替换即可
        matrix[l1][l2 + i] = matrix[r1-i][l2]
        matrix[r1 - i][l2] = matrix[r1][r2-i]
        matrix[r1][r2 - i] = matrix[l1+i][r2]
        matrix[l1 + i][r2] = tmp
    return
if __name__ == '__main__':
    matrix = read_input()
    ans = rotate(matrix)
    print(ans)
