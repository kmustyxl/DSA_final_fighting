#Step1：建立大根堆
#Step2：获取最后元素，与头部元素交换，利用heapify重新调整为大根堆，直至heapsize为0
def heapsort(arr):
    if arr is None or len(arr)<2:
        return
    else:
        for i in range(len(arr)): #建立一个大根堆
            heapinsert(arr, i)
        heapsize = len(arr)
        swap(arr, 0, heapsize-1)   #获取当前堆中最大值
        heapsize -= 1
        while heapsize > 0:
            heapify(arr, 0, heapsize) #重新调整为大根堆
            swap(arr, 0, heapsize-1)  #继续获取当前heapsize范围内的最大值
            heapsize -= 1
    return arr

def heapinsert(arr, index): #大根堆
    while arr[index] > arr[int((index-1)/2)]:
        swap(arr, index, int((index - 1)/2))
        index = int((index-1)/2)

def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def heapify(arr, index, heapsize):   #index为当前变化的数字（变小了），heapsize为目前已排好的大根堆的长度
    left = 2 * index + 1  #找到当前数字的左孩子
    while left < heapsize:  #防止越界 --*--:如果左孩子已经越界，即不存在左孩子，无需再下沉。
        if left + 1 < heapsize and arr[left + 1] > arr[left]: #判断是否有右孩子，并且找到左孩子和右孩子最大
            lagest = left + 1                                 #的那个，标志为lagest
        else:
            lagest = left
        if arr[lagest] <= arr[index]:  #如果lagest仍然小于等于变化的数字，无需下沉，直接break
            break
        else:
            swap(arr, index, lagest)   #否则，交换变化的数字和lagest，此时，index更新为lagest，继续往下判断
            index = lagest
            left = 2 * index + 1
arr = [3,4,5,6,2,1]
ans = heapsort(arr)
print(ans)