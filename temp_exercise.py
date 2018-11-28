def mergesort(arr,l,r):
    if l==r:
        return
    mid = l+int((r-l)/2)
    left = mergesort(arr,l,mid)
    right = mergesort(arr,mid+1,r)
    return merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    help_arr = []
    p0 = l
    p1 = mid + 1
    while p0 <= mid and p1 <= r:
        if arr[p0] < arr[p1]:
            help_arr.append(arr[p0])
            p0 += 1
        else:
            help_arr.append(arr[p1])
            p1 += 1
    while p0 <= mid:
        help_arr.append(arr[p0])
        p0 += 1
    while p1 <= r:
        help_arr.append(arr[p1])
        p1 += 1
    for i in range(len(help_arr)):
        arr[l+i] = help_arr[i]
    return arr

if __name__=='__main__':
    arr = [3,4,5,2,1,7,8]
    arr = mergesort(arr,0,len(arr)-1)
    print(arr)