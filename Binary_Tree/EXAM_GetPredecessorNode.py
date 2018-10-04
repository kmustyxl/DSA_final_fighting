class Node:
    def __init__(self,val=None,parent=None,lchild=None,rchild=None):
        self.val = val
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
def getPrecedessorNode(Node):
    if Node.val is None:
        return
    if Node.lchild is not None:
        Node = Node.lchild
        while Node.rchild is not None:
            Node = Node.rchild
        return Node
    else:
        parent = Node.parent
        while parent is not None and parent.rchild != Node:
            Node = parent
            parent = Node.parent
        return parent