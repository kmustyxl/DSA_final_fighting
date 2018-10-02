class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def ifcircle(head):
    '''
    判断链表是否有环
    :param head:
    :return:
    '''
    fast = head
    slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
    return None

def nocircle_firstnode(head1,head2):
    '''
    如果两个链表都无环。ps:一个有环链表和一个无环链表永远不可能相交，单链表的特性，只有一个next
    :param head1:
    :param head2:
    :return:
    '''
    len1 = 0
    len2 = 0
    last_node1 = head1
    last_node2 = head2
    while last_node1.next: #分别获取两个链表的长度和最后一个节点
        len1 += 1
        last_node1 = last_node1.next
    while last_node2.next:
        len2 += 1
        last_node2 = last_node2.next
    if last_node1 != last_node2: #如果两个链表的最后节点都不相同，则两个无环链表不存在交叉。
        return False
    if len1 == len2:             #如果两个链表最后的节点相同，说明有相交部分，但此时不能确定第一个相交节点位置
        while head1 != head2:    #如果两个链表长度相同，则同时从头结点开始，第一次遇到相同的节点，即为所求
            head1 = head1.next   #如果长度不同，则较长的那条链表先执行next abs(len1-len2)次，再一起next。
            head2 = head2.next
        return head1
    elif len1 > len2:
        for _ in range(len1-len2):
            head1 = head1.next
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1
    elif len1 < len2:
        for _ in range(len2-len1):
            head2 = head2.next
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1

def circle_firstnode(head1, head2):
    loop1 = ifcircle(head1)
    loop2 = ifcircle(head2)
    if loop1 == loop2 and loop1 == None:
        #两个链表均无环
        ans = nocircle_firstnode(head1, head2)
    elif (loop1 == None and loop2 != None) or (loop1 != None and loop2 == None):
        #一个链表有环，一个链表无环
        return None
    else:
        #两个链表都有环，分三种情况，1:两个链表不相交;2:两个链表的loop一样;3:两个链表的loop不一样
        if loop1 == loop2:
            pass#这种情况和无环一样，只是不考虑环部分
        while loop1.next != loop1:
            if loop1.next == loop2:
                #如果loop2出现在了loop1的环中，则为第三种情况，loop1和loop2都可以作为第一个相交的节点
                return loop1
            else:
                #如果loop2没有出现在loop1的环中，则两个有环链表不相交
                return None



