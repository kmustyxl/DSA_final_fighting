def merge_sort(arr, L, R):
    if L == R:
        return
    else:
        mid = int((L +R) / 2)
        merge_sort(arr, L, mid)
        merge_sort(arr, mid+1, R)
        return merge(arr, L, mid, R)

def merge(arr, L, mid, R):
    help = []
    p1 = L
    p2 = mid + 1
    while p1 <= mid and p2 <= R:
        if arr[p1] <= arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    while p1<= mid:
        help.append(arr[p1])
        p1 += 1
    while p2 <= R:              #执行完这两个while循环之一后，help数组已有序，但arr数组仍然保持之前状态
        help.append(arr[p2])
        p2 += 1
    for i in range(len(help)):
        arr[L + i] = help[i]   #help数组只是辅助数组，整个递归操作都是在围绕arr数组，因此需要将排序好的help数组
    return  help              #拷贝到arr数组
arr = [4,6,2,5,7,1]
demo = merge_sort(arr, 0, len(arr)-1)
print(demo)

