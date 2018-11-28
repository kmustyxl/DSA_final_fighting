def little_small(arr,l,r):
    '''
    date：2018-11-28
    小和问题：
    求一个数组中，左边小于右边的所有数的和。
    eg：[1,5,3,7,2]
        [1,5]:1
        [1,5,3]:1
        [1,5,3,7]:1,5,3
        [1,5,3,7,2]:1
        little_small=1+1+1+5+3+1
    思路：
    利用归并排序的merge操作，每一次merge的两部分都是内部有序的，则出现arr[p0]<arr[p1]时，只需统计右侧部分有几个比arr[p0]大的即可。
    '''
    if arr is None or len(arr) < 2:
        return
    if l == r:
        return arr[l]
    mid = l + int((r-l)/2)
    little_small(arr,l,mid)
    little_small(arr,mid+1,r)
    return merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    global small_sum
    p0 = l
    p1 = mid + 1
    help = []
    while p0 <= mid and p1 <= r:
        if arr[p0] < arr[p1]:
            small_sum += arr[p0] * int(r-p1+1)
            help.append(arr[p0])
            p0 += 1
        else:
            help.append(arr[p1])
            p1 += 1
    while p0 <= mid:
        help.append(arr[p0])
        p0 += 1
    while p1 <=r:
        help.append(arr[p1])
        p1 += 1
    for i in range(len(help)):
        arr[l+i] = help[i]
    return arr

if __name__ == '__main__':
    arr = [1,5,3,7,2]
    small_sum = 0
    ans = little_small(arr,0,len(arr)-1)
    print(small_sum)

