class Node:
    def __init__(self,val=None,lchild=None,rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
def SearilizationBinaryTree(Node):
    '''
    利用先序遍历的方式序列化二叉树
    :param Node:
    :return:
    '''
    if Node.val is None:
        return '#_'
    else:
        res = str(Node.val) + '_'
        res += SearilizationBinaryTree(Node.lchild)
        res += SearilizationBinaryTree(Node.rchild)
def ReconBinaryTree(String):
    String = String.strip().split('_')
    str_node = String.pop()
    if str_node == '#':
        return
    else:
        #首先建立头节点
        head = Node(int(str_node))
        #然后利用剩下的字符串依次构建左子树和右子树
        head.lchild = ReconBinaryTree(String)
        head.rchild = ReconBinaryTree(String)
