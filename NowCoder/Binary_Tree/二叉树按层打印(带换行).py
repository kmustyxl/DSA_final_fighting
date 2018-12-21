from NowCoder.Binary_Tree import Define_Binary_Tree as BT
class Node:
    def __init__(self,val=None,lchild=None,rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
def printBinaryTree(Node):
    '''
    按层打印二叉树，带换行
    :param Node:
    :return:
    '''
    if Node is None:
        return
    last = Node #last指每行最后节点
    nlast = Node #nlast永远指向队列中最新加入的节点
    queue = []
    queue.append(Node)
    while len(queue) != 0:
        Node = queue.pop(0)
        print(Node.val,end=' ')
        if Node.lchild is not None:
            queue.append(Node.lchild)
        if Node.rchild is not None:
            queue.append(Node.rchild)
        if len(queue) == 0:
            nlast = None
        else:
            nlast = queue[-1]
        if Node == last:
            #如果从队列中弹出的节点与last节点相同，last更新为nlast。
            last = nlast
            print('\t')
Tree = BT.Tree()
Tree.add(1)
Tree.add(2)
Tree.add(3)
Tree.add(4)
Tree.add(5)
Tree.add(6)
printBinaryTree(Tree.root)
