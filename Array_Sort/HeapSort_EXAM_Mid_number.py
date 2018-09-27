def Mid_number(arr):
    '''
    随时获取数据流中的中位数

    首先，需要建立一个大根堆和一个小根堆。 实时保证大根堆和小根堆的平衡，数量差值不能大于1
    大根堆存放数组中较小的部分，则堆顶就是较小部分的最大值
    小根堆存放数组中较大的部分，则堆顶就是较大部分的最小值
    :param arr:
    :return:
    '''
    if arr is None:
        return
    Big_heap = [] #建立大根堆
    Small_heap = [] #建立小根堆
    mid_num_arr = []
    Big_heap.append(arr[0]) #首先将第一个数放在大根堆中
    for i in range(1,len(arr)):
        if Big_heap[0] >= arr[i]: #如果数据流吐出的数字小于大根堆堆顶，则放入大根推
            Big_heap.append(arr[i])
            BigHeapinsert(Big_heap, len(Big_heap)-1) #调整大根堆结构，恢复大根堆结构
        else:
            Small_heap.append(arr[i]) #如果数据流吐出的数字大于大根堆堆顶，则放入小根推
            SmallHeapinsert(Small_heap, len(Small_heap)-1) #调整小根堆结构，恢复小根堆结构
        if len(Big_heap) - len(Small_heap) >= 2: #判断大小根堆规模差值是否大于1
            swap(Big_heap, 0, len(Big_heap)-1) #如果大根堆超，则将大根堆堆顶弹出
            heapsize = len(Big_heap)-1 #策略为：将堆顶与最后一个数交换位置
            BigHeapify(Big_heap,0,heapsize) #在heapsize范围上恢复大根堆
            remove_data = Big_heap.pop() #将弹出的堆顶数据放到小根堆
            Small_heap.append(remove_data)
            SmallHeapinsert(Small_heap, len(Small_heap) - 1)
        elif len(Small_heap) - len(Big_heap) >= 2: #小根堆的处理与大根堆同理
            swap(Small_heap, 0, len(Small_heap)-1)
            heapsize = len(Small_heap) - 1
            SmallHeapify(Small_heap, 0, heapsize)
            remove_data = Small_heap.pop()
            Big_heap.append(remove_data)
            BigHeapinsert(Big_heap, len(Big_heap)-1)
        if len(Big_heap) == len(Small_heap):
            mid_num = (Big_heap[0] + Small_heap[0]) / 2.0
        elif len(Big_heap) - len(Small_heap) == 1:
            mid_num = Big_heap[0]
        elif len(Big_heap) - len(Small_heap) == -1:
            mid_num = Small_heap[0]
        mid_num_arr.append(mid_num)
    return mid_num_arr

def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def BigHeapinsert(arr, index): #大根堆插入新的数据，并与父代依次比较，找到合适位置
    while arr[index] > arr[int((index-1)/2)]:
        swap(arr, index, int((index-1)/2))
        index = int((index-1)/2)

def SmallHeapinsert(arr,index):
    while arr[index] < arr[int((index-1)/2)]:
        swap(arr, index, int((index-1)/2))
        index = int((index-1)/2)

def BigHeapify(arr, index, heapsize): #大根堆的调整是将最后的子代和栈顶交换位置，此时‘临时栈顶’小于后代
    left = 2 * index + 1              #因次需要依次比较子代找到合适位置
    while left < heapsize:
        if left + 1 < heapsize and arr[left+1] > arr[left]:
            lagest = left + 1
        else:
            lagest = left
        swap(arr, index, lagest)
        index = lagest
        left = 2 * index + 1

def SmallHeapify(arr, index, heapsize):
    left = 2 * index + 1
    while left < heapsize:
        if left + 1 < heapsize and arr[left+1] < arr[left]:
            least = left + 1
        else:
            least = left
        swap(arr, index, least)
        index = least
        left = 2 * index + 1


