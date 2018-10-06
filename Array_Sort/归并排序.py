def Merge_sort(arr,l,r):
    if l == r:
        return
    mid = int((l + r)/2)
    Merge_sort(arr,l,mid)
    Merge_sort(arr,mid+1,r)
    return Merge(arr, l, mid, r)
def Merge(arr, l, mid, r):
    help = []
    p1 = l
    p2 = mid + 1
    while p1 <= mid and p2 <= r:
        if arr[p1] <= arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        help.append(arr[p1])
        p1 += 1
    while p2 <= r:
        help.append(arr[p2])
        p2 += 1
    for i in range(len(help)): #help只是个辅助数组，需要将数组拷贝到arr数组并返回。
        arr[l+i]  = help[i]
    return arr
arr = [1,3,4,3,2,1,9,6]
ans = Merge_sort(arr, 0, len(arr)-1)
print(ans)

