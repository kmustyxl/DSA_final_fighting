class Tree_Node:
    '''
    节点类
    '''
    def __init__(self,val=None,lchild=None,rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
class Tree:
    '''
    树类
    '''
    def __init__(self):
        self.root = Tree_Node()
        self.queue = []
    def add(self, val):
        '''
        为树添加节点
        '''
        treenode = Tree_Node(val)
        if self.root.val is None: #如果树是空的，则对树根节点进行赋值
            self.root = treenode
            self.queue.append(self.root)
        else:
            lst_treenode = self.queue[0] #queue[0]只保存当前子树的根节点
            if lst_treenode.lchild is None:
                lst_treenode.lchild = treenode
                self.queue.append(lst_treenode.lchild)
            else:
                lst_treenode.rchild = treenode
                self.queue.append(lst_treenode.rchild)
                self.queue.pop(0) #当子树的右节点不为空后，此二叉树满，pop子树根节点，新的根节点转移至左子树
    def preOrder_Recur(self,root):
        '''
        二叉树的先序遍历
        '''
        if root is None:
            return
        print(root.val)
        self.preOrder_Recur(root.lchild)
        self.preOrder_Recur(root.rchild)
    def inOrder_Recur(self,root):
        '''
        二叉树的中序遍历
        '''
        if root is None:
            return
        self.inOrder_Recur(root.lchild)
        print(root.val)
        self.inOrder_Recur(root.rchild)
    def posOrder_Recur(self,root):
        '''
        二叉树的后序遍历
        '''
        if root is None:
            return
        self.posOrder_Recur(root.lchild)
        self.posOrder_Recur(root.rchild)
        print(root.val)
    def preOrder_unRecur(self,root):
        '''
        非递归版的先序遍历，需利用堆栈
        '''
        if root is None:
            return
        Stack = []
        Stack.append(root) #首先将根节点入栈
        while len(Stack) != 0:
            root = Stack.pop()
            print(root.val)
            if root.rchild != None: #因为栈是后进先出，因此首先将右孩子入栈
                Stack.append(root.rchild)
            if root.lchild != None:
                Stack.append(root.lchild)
    def inOrder_unRecur(self, root):
        '''

        非递归版的中序遍历，需利用栈
        '''
        if root is None:
            return
        Stack = []
        while len(Stack) !=0 or root is not None: #因为中序遍历要先遍历左孩子因此，左孩子若存在则一直入栈
            if root is not None:
                Stack.append(root)
                root = root.lchild
            else:
                root = Stack.pop()  #当左孩子为空时，弹出栈顶，打印，然后转至右孩子，再判断右孩子是否为空以及它的左孩子。
                print(root.val)
                root = root.rchild
    def posOrder_unRecur(self,root):
        '''
        先序遍历的顺序为根->左->右。因为遇到根节点就直接打印了，所以入栈顺序为根，右，左
        而后序遍历的顺序恰好为左、右、根。因此，利用两个栈，将前序遍历的结果压入辅助栈，再弹出就变成了后序遍历
        tips:先序遍历先压右孩子，再压左孩子；然后弹出时为左右。后序遍历因为用到了两个栈，因此要先压左孩子，再压右孩子
        然后以右左的顺序压入第二个栈，再弹出时才是左右的顺序。
        '''
        if root is None:
            return
        Stack1 = []
        Stack2 = []
        Stack1.append(root)
        while len(Stack1) != 0:
            root = Stack1.pop()
            Stack2.append(root)
            if root.lchild is not None:
                Stack1.append(root.lchild)
            if root.rchild is not None:
                Stack1.append(root.rchild)
        while len(Stack2) != 0:
            root = Stack2.pop()
            print(root.val)
    def levelOrder_unRecur(self,root):
        '''
        利用层次遍历，需要利用队列
        :param root:
        :return:
        '''
        if root is None:
            return
        queue = []
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.val)
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)
# ans = Tree()
# ans.add(1)
# ans.add(2)
# ans.add(3)
# ans.add(4)
# print(ans.root.lchild.val)
# ans.levelOrder_unRecur(ans.root)




