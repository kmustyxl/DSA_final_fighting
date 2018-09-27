def MaxGap(arr):
    arr.sort()
    min_num = min(arr)
    max_num = max(arr)
    num_num = len(arr)
    Gap_list = []
    if min_num == max_num:
        return 0
    distance = (max_num - min_num) / num_num
    bucket = [[0,None,None] for i in range(num_num + 1)] #三个变量分别存放布尔类型(0为空桶，1为非空桶)
    for i in range(num_num):                      #第二个变量存放最小值，第三个变量存放最大值。
        index = int((arr[i] - min_num) / distance)
        bucket[index][0] = 1
        if bucket[index][1] is None:
            bucket[index][1] = arr[i]
            bucket[index][2] = arr[i]
        else:
            if arr[i] < bucket[index][1]:
                bucket[index][1] = arr[i]
            elif arr[i] > bucket[index][2]:
                bucket[index][2] = arr[i]
            else:
                continue
    bucket_gap = 1
    for i in range(1,num_num+1):
        if bucket[i][0] == 0:
            bucket_gap += 1
            continue
        Cur_gap = int(bucket[i][1] - bucket[i-bucket_gap][2])
        Gap_list.append(Cur_gap)
        bucket_gap = 1
    Max_gap = max(Gap_list)
    return Max_gap

