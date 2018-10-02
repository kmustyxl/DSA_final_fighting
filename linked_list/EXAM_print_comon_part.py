class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
def print_comon_part(node1, node2):
    '''
    给定两个有序链表的头结点head1和head2，，打印两个有序链表的公共部分
    :param node1:
    :param node2:
    :return:
    '''
    while node1 and node2:
        if node1.val < node2.val:
            node1 = node1.next
        elif node1.val > node2.val:
            node2 = node2.next
        else:
            print(node1.val)
            node1 = node1.next
            node2 = node2.next
