def Permutation(arr, begin, end):
    if begin >= end:
        print(arr)
        global  count
        count += 1
        return
    for num in range(begin,end):
        #递归思路:每次取出第一个元素放到最后，即arr[begin]与arr[num]交换，然后num+1，扩充范围直至end；
        #然后begin指针+1，重复上述步骤。
        arr[num], arr[begin] = arr[begin], arr[num]
        Permutation(arr, begin+1, end)
        arr[num], arr[begin] = arr[begin], arr[num]
arr = [1,2,3,4]
count = 0
Permutation(arr, 0, 4)
print(count)