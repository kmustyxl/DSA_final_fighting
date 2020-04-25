A=[4,3,9,10,2,4,11,7]

def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b

def insert_sort(A):
    for i in range(1,len(A)):
        for j in range(i)[::-1]:
            if A[j+1] <= A[j]:
                A[j],A[j+1] = swap(A[j],A[j+1])
            else:
                break
    return A

B=insert_sort(A)
print(B)
