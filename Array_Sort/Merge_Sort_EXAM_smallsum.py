def small_sum(arr):
    if len(arr) <= 1:
        return 0
    else:
        return merge_sort(arr, 0, len(arr)-1)

def merge_sort(arr, l, r):
    if l == r:
        return 0
    else:
        mid = int((l + r) / 2)
        return merge_sort(arr, l, mid) + merge_sort(arr, mid+1, r) + merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    help = []
    p1 = l
    p2 = mid + 1
    res = 0
    while p1 <= mid and p2 <= r:
        if arr[p1] < arr[p2]:
            res += arr[p1] * len(arr[p2:])
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
    for i in range(len(help)):
        arr[l + i] = help[i]
    return res
