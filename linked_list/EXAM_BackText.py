class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
def Use_stack(head):
    stack = []
    cur = head
    while cur:
        stack.append(cur.next)
        cur = cur.next
    while head:
        if head.val != stack.pop().val:
            return False
        head = head.next
    return True

def Back_text(head):
    '''
    额外空间为O(1)
    :param head:
    :return:
    '''
    if head is None or head.next is None:
        return True
    n1 = ListNode()
    n2 = ListNode()
    n1 = head #慢指针
    n2 = head #快指针
    while n2.next and n2.next.next:
        n1 = n1.next
        n2 = n2.next.next
    n2 = n1.next #n2为右半部分第一个节点 p
    n1.next = None #中点的节点指向空 pre
    n3 = ListNode()
    n3 = None # cur
    while n2: #右半部分逆序
        n3 = n2.next #存储下一个节点
        n2.next = n1 #存储上一个节点
        n1 = n2 #存储当前节点
        n2 = n3 #将下一个节点作为当前节点
    n3 = n1 #n3存储最后一个节点
    n2 = head
    index = True
    while n1 is not None and n2 is not None:
        if n1.val != n2.val:
            index = False
            break
        n1 = n1.next
        n2 = n2.next
    n1 = n3.next #当前节点
    n3.next = None
    while n1:
        n2 = n1.next #存储下一个节点
        n1.next = n3 #存储上一个节点
        n3 = n1 #存储当前节点
        n1 = n2 #下一个节点作为当前节点


