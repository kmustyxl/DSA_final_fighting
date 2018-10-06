def InsertSort(arr):
    '''
    模拟洗牌动作，从右往左
    :param arr:
    :return:
    '''
    len_arr = len(arr)
    for i in range(1,len_arr):
        index_card = arr[i]
        for j in range(i)[::-1]:
            if index_card < arr[j]:
                swap(arr, j, j+1)
    return arr
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

arr = [3,3,2,1,8,5,0,9,-1]
ans = InsertSort(arr)
print(ans)