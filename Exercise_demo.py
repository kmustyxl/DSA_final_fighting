def bucketsort(array,arr_min,arr_max):
    if array is None or len(array) < 2:
        return array
    arr_sort = []
    bucket_num = int(arr_max - arr_min + 1)
    bucket_arr = [0 for i in range(bucket_num)]
    for i in range(len(array)):
        bucket_arr[array[i] - arr_min] += 1
    for i in range(bucket_num):
        if bucket_arr[i] == 0:
            continue
        for _ in range(bucket_arr[i]):
            arr_sort.append(int(i+arr_min))
    return arr_sort
if __name__ == "__main__":
    array = [5,2,1,8,35,12,4]
    arr_min = min(array)
    arr_max = max(array)
    arr_sort = bucketsort(array,arr_min,arr_max)
    print(arr_sort)
