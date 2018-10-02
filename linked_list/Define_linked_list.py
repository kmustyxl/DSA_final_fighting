class linked_Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class linked_list(linked_Node):
    def __init__(self):
        self.head = None  #头结点也是一个结点结构
        self.length = 0
    def isEmpty(self):
        return (self.length == 0)
    def add(self,dataOrNode): #加入的是一个新的结点,在链表最后加
        item = None
        if isinstance(dataOrNode, linked_Node):
            item = dataOrNode
        else:
            item = linked_Node(dataOrNode)
        if not self.head: #如果链表的头为空
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1
    def delete(self, index): #删除的是一个结点
        if self.isEmpty():
            print('linkedlist is empty')
            return
        if index < 0 or index >=self.length:
            print('index out of linked_list range')
            return
        if index == 0:
            #如果删除的是第一个结点
            self.head = self.head.next
            self.lenght -= 1
        else:
            j = 0
            node = self.head #初始化；node保存当前结点
            prev = self.head #初始化；prev保存前导结点
            while node.next and j < index:
                prev = node
                node = prev.next
                j += 1
            if j == index:
                prev.next = node.next
                self.length -= 1
    def update(self, index, data): #更新的是一个数据值
        if self.isEmpty() or index < 0 or index >= self.length:
            print('index out of linked_list range')
            return
        else:
            j = 0
            node = self.head
            while self.next and j < index:
                node = node.next
                j += 1
            if j == index:
                node.val = data
    def getitem(self, index): #查找一个节点
        if self.isEmpty() or index < 0 or index >= self.length:
            print('index out of linked_list range')
            return
        else:
            j = 0
            node = self.head
            while node.next and j < index:
                node = node.next
                j += 1
            return node.val
    def print_linkedlist(self):
        if self.isEmpty():
            print('linked_list is empty')
            return
        j = 0
        ans_arr = []
        node = self.head
        while node:
            ans_arr.append(node)
            node = node.next
        return ans_arr
    def getIndex(self, data):
        if self.isEmpty():
            print('linked_list is empty')
            return
        j = 0
        node = self.head
        while node:
            if node.val == data:
                return j
            node = node.next
            j += 1
            if j == self.length:
                print('%s is not found'%data)
                return
    def insert(self, index, dataOrNode):
        if self.isEmpty() or index < 0 or index >= self.length:
            print('index is out of linked_list range')
        item = None
        if isinstance(dataOrNode, linked_Node):
            item = dataOrNode
        else:
            item = linked_Node(dataOrNode)
        if index == 0:
            item.next = self.head
            self.head = item
            self.length += 1
            return
        j = 0
        prev = self.head
        node = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1
        if j == index:
            item.next = node
            prev.next = item
            self.length += 1


ans = linked_list()
ans.add(5)
ans.add(6)
an = ans.print_linkedlist()
print(an)