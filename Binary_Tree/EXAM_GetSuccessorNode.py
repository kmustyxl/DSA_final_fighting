class Node:
    def __init__(self,val=None,parent=None,lchild=None,rchild=None):
        self.val= val
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
def getSuccessorNode(Node):
    '''
    在二叉树中找一个节点的后继节点
    :param Node:
    :return:
    '''
    if Node.val is None:
        return
    if Node.rchild is not None: #如果待查找节点存在右孩子，则找到右子树的最左节点返回即可
        Node = Node.rchild
        while Node.left is not None:
            Node = Node.left
        return Node
    else:
        parent = Node.parent
        while parent.val is not None and parent.lchild != Node:
        #如果不存在右节点，则需判断父节点，如果当前节点为父节点的左孩子，直接返回父节点；
        #如果不是左孩子，则层层往上找，直到找到当前节点为父节点的左孩子时，返回此时的父节点即为后继节点。
            Node = parent
            parent = Node.parent
        return parent

