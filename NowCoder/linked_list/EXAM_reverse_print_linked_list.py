class listnode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def reverse_print(linkedlist):
    '''
    使用栈
    :param linkedlist:
    :return:
    '''
    res_arr = []
    node = linkedlist
    while node.next:
        res_arr.append(node.val)
        node = node.next
    res_arr.reverse()
    return res_arr

def recursive_print(linkedlist):
    '''
    使用递归，先输出后面的节点，再输出节点自身
    :param linkedlist:
    :return:
    '''
    if not linkedlist:
        return []
    else:
        recursive_print(linkedlist.next) + [linkedlist.val]


