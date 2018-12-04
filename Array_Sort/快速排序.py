import random
def quicksort(arr,l,r):
    if arr is None or l==r:
        return
    if l < r:
        random_seed = l + int((r-l)*random.random())
        swap(arr,random_seed,r)
        p = partition(arr,l,r)
        quicksort(arr,l,p[0]-1)
        quicksort(arr,p[1]+1,r)
        return arr

def partition(arr,l,r):
    less = l - 1
    more = r
    while l < more:
        if arr[l] <arr[r]:
            swap(arr,less+1,l)
            less += 1
            l += 1
        elif arr[l] == arr[r]:
            l += 1
        else:
            swap(arr,l,more-1)
            more -= 1
    swap(arr,r,more)
    return [less+1,more]


def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

if __name__ == '__main__':
    arr = [12,2,4,1,2,6,8,5,-2]
    ans = quicksort(arr,0,len(arr)-1)
    print(ans)