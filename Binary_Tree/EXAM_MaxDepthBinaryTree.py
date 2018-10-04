class Node:
    def __init__(self,val=None,lchild=None,rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
def MaxDepthBinaryTree(Node):
    if Node is None:
        return 0
    else:
        left = MaxDepthBinaryTree(Node.lchild)
        right = MaxDepthBinaryTree(Node.rchild)
        return max(left,right) + 1