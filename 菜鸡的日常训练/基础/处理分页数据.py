class Node:
    def __init__(self, value):
        self.value = value  # 信息域
        self.next = None  # 指针域


class SingleLinkedList:
    def __init__(self, node=None):
        """创建一个单链表对象,if 不传入头结点,则创建空链表"""
        self.__head = node

    def is_empty(self):
        """判断是否为空链表"""
        return self.__head is None

    def length(self):
        count = 0
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next  # 向后移动游标
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head  # 游标，用来表示当前节点
        while cur is not None:
            yield cur.value  # 生成当前节点的值
            cur = cur.next  # 向后移动游标

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur is not None:
                cur = cur.next
            cur.next = node
