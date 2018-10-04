class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.lchild = left
        self.rchild = right
def SerializationBinaryTree(Node):
    '''
    二叉树序列化
    :param Node:
    :return:
    '''
    if Node is None:
        return '#_'
    else:
        res = str(Node.val) + '_'
        res += SerializationBinaryTree(Node.lchild)
        res += SerializationBinaryTree(Node.rchild)
    return res
def ReconBinaryTree(Str_queue):
    '''
    利用前序遍历重建二叉树
    :param Str_queue:
    :return:
    '''
    Str_queue = Str_queue.split('_')
    str_node = Str_queue.pop(0)
    if str_node == '#':
        return
    else:
        head = Node(int(str_node))
        head.lchild = ReconBinaryTree(Str_queue)
        head.rchild = ReconBinaryTree(Str_queue)
    return head


