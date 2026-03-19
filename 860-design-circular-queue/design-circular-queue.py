class MyCircularQueue(object):

    def __init__(self, k):
        self.q = [0] * k  # фиксированный массив
        self.size = k
        self.head = 0  # начало очереди
        self.tail = 0  # куда вставляем
        self.count = 0  # количество элементов

    def enQueue(self, value):
        if self.count == self.size:  # очередь полная
            return False

        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.size  # переход по кругу
        self.count += 1
        return True

    def deQueue(self):
        if self.count == 0:  # очередь пустая
            return False

        self.head = (self.head + 1) % self.size  # просто двигаем head
        self.count -= 1
        return True

    def Front(self):
        if self.count == 0:
            return -1
        return self.q[self.head]  # первый элемент

    def Rear(self):
        if self.count == 0:
            return -1
        return self.q[(self.tail - 1) % self.size]  # последний элемент

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size