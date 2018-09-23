import random
def quick_sort(arr, l, r):
    if arr == None or len(arr) < 2:
        return
    else:
        return quickprocess(arr, l, r)

def quickprocess(arr, l , r):
    if l < r: #算法执行的前提是l < r
        random_index = l + int(random.random() * (r - l + 1)) #随机快排
        arr[random_index], arr[r] = swap(arr[random_index], arr[r])
        p = partition(arr, l , r) #找到与目标值相等的区间
        quickprocess(arr, l, p[0] - 1) #递归处理数组中小于目标值的片段
        quickprocess(arr, p[1] + 1, r) #然后递归处理数组中大于目标值的片段
    return arr

def partition(arr, l, r):
    less = l - 1
    more = r
    while l < more:  #l < more表示相等片段和大于片段之间还存在待比较片段
        if arr[l] < arr[r]:
            arr[less + 1], arr[l] = swap(arr[less + 1], arr[l]) #less与l之间可能已经存在了等于目标值的数组片段
            less += 1
            l += 1
        elif arr[l] == arr[r]:
            l += 1
        else:
            arr[more - 1], arr[l] = swap(arr[more - 1], arr[l])
            more -= 1 #与大于片段的左一数据交换后，因为这个交换的数据是待比较片段的，因此指针l不能加一，仍需继续比较交换过来的这个数据
    arr[more], arr[r] = swap(arr[more], arr[r]) #因为我们最开始就是以数组最右端的数据作为目标值的，因此需要将这个数据与more指针所指的数据交换
    return [less + 1, more]

def swap(data1, data2):
    temp = data1
    data1 = data2
    data2 = temp
    return data1, data2