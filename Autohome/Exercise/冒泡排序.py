A=[4,3,9,10,2,4,11,7]

def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b

def bubble_sort1(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j]>=A[j+1]:
                A[j],A[j+1] = swap(A[j],A[j+1])
    return A

def  bubble_sort2(A):
    for i in range(len(A))[::-1]:
        for j in range(i):
            if A[j]>=A[j+1]:
                A[j], A[j + 1] = swap(A[j], A[j + 1])
    return A

B=bubble_sort2(A)
print(B)