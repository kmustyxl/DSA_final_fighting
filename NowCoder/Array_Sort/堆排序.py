def HeapSort(arr):
    if arr is None or len(arr)<2:
        return
    for i in range(len(arr)):
        heapinsert(arr, i)
    heapsize = len(arr)
    swap(arr, 0, heapsize-1)
    heapsize -= 1
    while heapsize > 0:
        heapify(arr, 0, heapsize)
        swap(arr, 0, heapsize-1)
        heapsize -= 1
    return arr
def heapinsert(arr, index):
    while arr[index] > arr[int((index-1)/2)]:
        swap(arr, index, int((index-1)/2))
        index = int((index-1)/2)
def heapify(arr, index, heapsize):
    left = 2 * index + 1
    while left < heapsize:
        if left + 1 < heapsize and arr[left+1]>arr[left]:
            lagest = left + 1
        else:
            lagest = left
        if arr[index] < arr[lagest]:
            swap(arr, index, lagest)
            index = lagest
            left = 2 * index + 1
        else:
            break
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

arr = [1,2,3,4,3,2,1]
ans = HeapSort(arr)
print(ans)
