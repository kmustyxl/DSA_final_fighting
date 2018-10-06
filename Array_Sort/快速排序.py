import random
def QuickSort(arr,l,r):
    if l == r:
        return
    if l < r:
        random_index = l + int((r-l+1)*random.random())
        swap(arr, l, random_index)
        p = partition(arr, l, r)
        QuickSort(arr, l, p[0])
        QuickSort(arr, p[0]+1, r)
    return arr
def partition(arr, l, r):
    less = l-1
    more = r
    while l < more:
        if arr[l] < arr[r]:
            swap(arr, less+1, l)
            less += 1
            l += 1
        elif arr[l] == arr[r]:
            l += 1
        else:
            swap(arr, l, more-1)
            more -=1
    swap(arr, more, r)
    return [less+1, more-1]

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
arr = [1,4,3,4,5,1,8,0,9]
ans = QuickSort(arr, 0, len(arr)-1)
print(ans)

