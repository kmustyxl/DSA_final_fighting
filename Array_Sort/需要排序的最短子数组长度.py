def getMinSortLength(arr):
    if arr is None or len(arr) < 2:
        return 0
    max_num = arr[0]
    noMaxIndex = -1
    for i in range(1, len(arr)):
        if arr[i] < max_num:
            noMaxIndex = i
        else:
            max_num = max(arr[i], max_num)
    min_num = arr[-1]
    noMinIndex = -1
    for i in range(len(arr)-2)[::-1]:
        if arr[i] > min_num:
            noMinIndex = i
        else:
            min_num = min(arr[i], min_num)
    if noMinIndex == -1:
        return 0
    else:
        return noMaxIndex - noMinIndex + 1
arr = [1,2,3]
ans = getMinSortLength(arr)
print(ans)

