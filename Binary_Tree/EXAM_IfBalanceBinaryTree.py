from Binary_Tree import Define_Binary_Tree as BT
class Node:
    def __init__(self,val=None,lchild=None,rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
class returnans:
    def __init__(self, ifB=None, h=None):
        self.ifB = ifB
        self.h = h
def IfBalanceBinaryTree(Node):
    if Node.val is None:
    #判断树是否为空
        return returnans(True, 0)
    leftData = IfBalanceBinaryTree(Node.lchild)
    if leftData.ifB == False:
        #如果左树不是平衡的直接返回
        return returnans(False, 0)
    rightData = IfBalanceBinaryTree(Node.rchild)
    if rightData.ifB == False:
        #如果右树不是平衡的直接返回
        return returnans(False, 0)
    if abs(leftData.h - rightData.h) > 1:
        #如果左右树都是平衡树，则需判断左右子树的高度差是否满足<=1
        return returnans(False, 0)
    else:
        #如果满足<= 1,则返回当前树的高度，继续递归
        return returnans(True, max(leftData.h, rightData.h) + 1)
ANS = BT.Tree()
return_ans = IfBalanceBinaryTree(ANS.root)
print(return_ans.ifB, return_ans.h)

