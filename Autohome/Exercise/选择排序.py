A=[4,3,9,10,2,4,11,7]

def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b

def choose_sort(A):
    for i in range(len(A)):
        least = i
        for j in range(i,len(A)):
            if A[j]<=A[least]:
                least = j
            else:
                continue
        A[i],A[least] = swap(A[i],A[least])
    return A

B=choose_sort(A)
print(B)