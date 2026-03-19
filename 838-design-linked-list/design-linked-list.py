class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None  # ссылка на следующий элемент


class MyLinkedList(object):

    def __init__(self):
        self.head = None  # начало списка

    def get(self, index):
        cur = self.head
        for i in range(index):
            if not cur:
                return -1
            cur = cur.next  # идём по списку
        if cur:
            return cur.val
        return -1

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head  # новый элемент указывает на старый
        self.head = node

    def addAtTail(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next  # идём до конца
        cur.next = node  # добавляем в конец

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for i in range(index - 1):
            if not cur:
                return
            cur = cur.next
        if cur:
            node = Node(val)
            node.next = cur.next  # вставка между элементами
            cur.next = node

    def deleteAtIndex(self, index):
        if index == 0 and self.head:
            self.head = self.head.next  # удаляем голову
            return
        cur = self.head
        for i in range(index - 1):
            if not cur:
                return
            cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next  # "перепрыгиваем" элемент