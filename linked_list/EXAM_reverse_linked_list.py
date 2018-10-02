class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
def reverse(head):
    if head is None:
        return
    else:
        p = head #当前节点
        pre = None #存储上一个节点，存储上一个节点是为了改指针
        cur = None #存储下一个节点，存储下一个节点是为了防止链表断开
        while p is not None:
            cur = p.next #先存储下一个节点
            p.next = pre #用释放的内存存储上一个节点
            pre = p #用释放的内存存储当前节点
            p = cur #将下一个节点作为当前节点重复操作
    return pre