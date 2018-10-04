class Node:
    def __init__(self,val=None,lchild=None,rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
def IfCompleteBinaryTree(Node):
    '''
    利用层次遍历来判断是否为完全二叉树。总结为两点：
    Tip1：如果一个节点存在右子树而不存在左子树，直接返回False
    Tip2：如果有一个节点无左右子树或只有左子树，则该节点接下来层次遍历的所有节点必须都满足无左右子树，否则返回False
    :param Node:
    :return:
    '''
    if Node.val is None:
        return True
    queue = []
    queue.append(Node)
    Index = False
    while len(queue) != 0:
        Node = queue.pop(0)
        if Node.lchild is not None:
            queue.append(Node.lchild)
        if Node.rchild is not None:
            queue.append(Node.rchild)
        if Node.lchild is None and Node.rchild is not None:
            return False
        if (Node.lchild is not None and Node.rchild is None) or \
            (Node.lchild is None and Node.rchild is None):
            Index = True
            continue
        if Index:
            if Node.lchild != None or Node.rchild != None:
                return False
    return  True
