class Node:
    def __init__(self, val=None, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
def IfBinarySearchTree(Node):
    '''
    判断一棵树是否为二叉搜索树，只需利用中序遍历的方式进行遍历，如果存在i<i-1的情况,则不是二叉搜索树
    :param Node:
    :return:
    '''
    if Node.val is None:
        return
    Stack1 = []
    Stack1.append(Node)
    judge_arr = []
    i = 0
    while len(Stack1) != 0 or Node.lchild is not None:
        if Node.lchild is not None:
            Stack1.append(Node.lchild)
            Node = Node.lchild
        else:
            Node = Stack1.pop()
            #print(Node.val)
            judge_arr.append(Node.val)
            i += 1
            Node = Node.rchild
            if len(judge_arr) <= 1:
                continue
            else:
                if judge_arr[i-1] < judge_arr[i-2]:
                    return False
    return True

