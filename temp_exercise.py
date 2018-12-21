#数据流中的中位数
def big_heap(arr,i):
    while arr[i] > arr[int((i-1)/2)]:
        swap(arr,i,int((i-1)/2))
        i = int((i-1)/2)
def big_heapfiy(arr,index,heapsize):
    left = 2 * index + 1
    while left < heapsize:
        if left + 1 < heapsize and arr[left + 1] > arr[left]:
            lagest = left + 1
        else:
            lagest = left
        if arr[index] >= arr[lagest]:
            break
        else:
            swap(arr,index,lagest)
            index = lagest
            left = 2 * index + 1
def small_heap(arr,i):
    while arr[i] < arr[int((i-1)/2)]:
        swap(arr,i,int((i-1)/2))
        i = int((i-1)/2)
def small_heapfiy(arr,index,heapsize):
    left = 2 * index + 1
    while left < heapsize:
        if left + 1 < heapsize and arr[left + 1] < arr[left]:
            least = left + 1
        else:
            least = left
        if arr[index] <= arr[least]:
            break
        else:
            swap(arr,index,least)
            index = least
            left = 2 * index + 1
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
def middle_num(arr):
    big_arr = []
    small_arr = []
    big_arr.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] <= big_arr[0]:
            big_arr.append(arr[i])
            big_heap(big_arr,len(big_arr)-1)
        else:
            small_arr.append(arr[i])
            small_heap(small_arr,len(small_arr)-1)
        if len(big_arr) - len(small_arr) >= 2:
            swap(big_arr,0,len(big_arr)-1)
            temp = big_arr.pop()
            big_heapfiy(big_arr,0,len(big_arr))
            small_arr.append(temp)
            small_heap(small_arr, len(small_arr) - 1)
        elif len(big_arr) - len(small_arr) <= 2:
            swap(small_arr,0,len(small_arr)-1)
            temp = small_arr.pop()
            small_heapfiy(small_arr,0,len(small_arr))
            big_arr.append(temp)
            big_heap(big_arr,len(big_arr)-1)
    if len(big_arr) == len(small_arr):
        return int(big_arr[0]+small_arr[0])/2
    elif len(big_arr) - len(small_arr) == 1:
        return int(big_arr[0])
    elif len(big_arr) - len(small_arr) == -1:
        return int(small_arr[0])


if __name__ == '__main__':
    arr = [11,1,3,9,5,10]
    ans = middle_num(arr)
    print(ans)
