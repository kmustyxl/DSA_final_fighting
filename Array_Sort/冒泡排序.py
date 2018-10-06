def BubbleSort(arr):
    '''
    模拟冒泡过程，从下往上
    :param arr:
    :return:
    '''
    num_arr = len(arr)
    for i in range(num_arr-1):
        for j in range(num_arr-i-1):
            if arr[j+1] <= arr[j]:
                swap(arr, j+1, j)
    return arr
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
arr = [3,3,2,1,8,5,0,9]
ans = BubbleSort(arr)
print(ans)