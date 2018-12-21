def mergeReverse(arr,l,r):
    '''
    打印数组中所有逆序对，和小和问题思想一致，小和问题为左边比右边小，即升序。逆序对则降序；

    '''
    if l == r:
        return
    else:
        mid = l + int((r-l)>>1)
        mergeReverse(arr,l,mid)
        mergeReverse(arr,mid+1,r)
        merge(arr,l,mid,r)
        return
def merge(arr,l,mid,r):
    p0 = l
    p1 = mid + 1
    help = []
    while p0 <= mid and p1 <= r:
        if arr[p0] <= arr[p1]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p0])
            #如果p0>p1,则p0大于arr[p1~r]的所有数，均可构成逆序对，不然会漏解
            for _ in range(p1,r+1):
                print([arr[p0], arr[_]])
            p0 += 1
    while p0 <= mid:
        help.append(arr[p0])
        p0 += 1
    while p1 <= r:
        help.append(arr[p1])
        p1 += 1
    for i in range(len(help)):
        arr[l + i] = help[i]
    return arr

if __name__ == '__main__':
    arr = [9,8,7,6,5,4]
    mergeReverse(arr,0,len(arr)-1)
