class Node(object):
    """
    定义结点
    """
    def __init__(self,item):
        self.item = item #存储具体元素
        self.next = None #存储下一个结点的内存地址

class SingleLinkList(object):
    def __init__(self):
        self._head = None #初始化链表
    def is_empty(self):
        """
        判断单链表是否为空
        """
        return self._head is None 
    def length(self):
        """
        获取链表长度
        """
        cur = self._head #获取头指针
        count = 0
        while cur.next is not None:
            count += 1
            cur = cur.next
    def items(self):
        """
        遍历单链表
        """
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next
    def add(self,item):
        node = Node(item) #生成一个结点
        #新结点指向头部结点
        node.next = self._head
        #头部结点修改为新结点
        self._head = node
    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    def insert(self,index,item):
        if(index <= 0): #如果是在头部插入
            self.add(item)
        elif index > (self.length -1): #如果是在尾部插入
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            for i in range(index -1):
                cur = cur.next
            node.next = cur.next 
            cur.next = node
    def remove(self,item):
        cur = self._head
        pre = None #上一个结点
        while cur is not None:
            if cur.item == item:
                if not pre: #如果头部即需要删除的结点
                    self._head = cur.next
                else: #原始序列pre.next = cur
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next
    def find(self,item):
        return item in self.items()

if __name__ == "__main__":
    link_list = SingleLinkList()
    for i in range(5):
        link_list.append(i)
    link_list.add(5)
    for i in link_list.items():
        print(i)