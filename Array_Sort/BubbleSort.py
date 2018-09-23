def BubbleSort(array): #O(N^2) 严格意义下的复杂度
    len_array = len(array)
    for i in range(len_array)[::-1]:
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = swap(array[j],array[j+1])
    return array
def swap(data1, data2):
    temp = data1
    data1 = data2
    data2 = temp
    return data1, data2