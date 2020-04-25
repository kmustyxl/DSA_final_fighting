A=[3,5,6,9,10,32]
B=[2,7,6,9,15,23]
#tip1：将B的每个元素在A遍历一遍
#tip2：将B的每个元素在A中进行二分查找
#tip3：类似外排的方式进行查找
def function3(A,B):
    len_A = len(A)
    len_B = len(B)
    A_index = 0
    B_index = 0
    switch = True
    target_list = []
    while switch:
        if A_index< len_A and B_index < len_B:
            if B[B_index]<= A[A_index]:
                if B[B_index]< A[A_index]:
                    target_list.append(B[B_index])
                B_index += 1
            else:
                A_index += 1
        else:
            switch = False
    for index in range(B_index,len_B):
        target_list.append(B[index])
    return target_list

target_list = function3(A,B)
print(target_list)