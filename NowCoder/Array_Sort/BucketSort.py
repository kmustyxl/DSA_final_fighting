def bucketsort(arr, min_num, max_num):
    bucket = [0 for i in range(min_num, max_num + 1)]
    sort_arr = []
    for i in range(len(arr)):
        bucket[arr[i]-min_num] += 1
    for i in range(len(bucket)):
        if bucket[i] == 0:
            continue
        for _ in range(bucket[i]):
            sort_arr.append(int(i + min_num))
    return sort_arr


