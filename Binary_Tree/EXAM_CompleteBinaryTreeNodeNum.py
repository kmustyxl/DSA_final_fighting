class Node:
    def __init__(self,val=None,lchild=None,rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
def CompleteBinaryTreeNodeNum(head):
    if head.val is None:
        return 0
    else:
        return bs(head, 1, mostleftlevel(head, 1))
def bs(node, level, h):
    if level == h: #如果当前节点的层数等于最大深度，那该节点就是叶节点，return 1
        return 1
    else:
        if mostleftlevel(node.right, level+1) == h:
            #判断右子树是否到达整棵树的最大深度h，如果满足，则左子树为满二叉树，此时递归求解右子树
            return 2^(h-level) + bs(node.rchild, level+1, h)
        else:
            #如果未达到最大深度，则右子树为深度为h-level-1的满二叉树，此时递归求解左子树
            return 2^(h-level-1) + bs(node.lchild, level+1, h)

def mostleftlevel(node, level):
    '''
    返回以当前节点为根的子树的最大深度
    :param node: 当前节点
    :param level: 当前节点所在层
    :return:
    '''
    if node.val is not None:
        level += 1
        node = node.lchild
    return level - 1