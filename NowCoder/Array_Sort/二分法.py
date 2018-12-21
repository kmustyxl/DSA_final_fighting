def BinarySearch(arr, key):
    if len(arr) == 0:
        return
    mid = int(len(arr)/2)
    l = 0
    r = len(arr) - 1
    while l <= r:
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            r = mid -1
        else:
            l = mid + 1
        mid = int((l + r)/2)
    return
arr = [1,2,3,4,5]
ans = BinarySearch(arr, 3)
print(ans)