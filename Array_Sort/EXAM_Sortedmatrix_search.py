def Sortedmatrix_search(matrix, k):
    N = len(matrix)
    M = len(matrix[0])
    i = 0
    j = M -1
    for _ in range(N+M-1):
        if matrix[i][j] == k:
            return True
        elif matrix[i][j] > k and j >= 1:
            j -= 1
        elif matrix[i][j] < k and i < N-1:
            i += 1
        else:
            return False
demo = [[1,2,3,4],[3,4,6,7],[5,8,9,11]]
ans = Sortedmatrix_search(demo, 1)
print(ans)