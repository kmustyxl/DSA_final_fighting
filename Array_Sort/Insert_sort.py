def Insert_sort(array): #O(N^2) 非严格意义下（如果已经排好序的数列复杂度将为O(N)）
    len_array = len(array)
    for i in range(len_array):
        for j in range(1 ,i+1)[::-1]:#设置1防止下溢
            if array[j] < array[j-1]:
                array[j], array[j-1] = swap(array[j], array[j-1])
            else:
                break
    return array
def swap(data1, data2):
    temp = data1
    data1 = data2
    data2 = temp
    return data1, data2
