class MyQueue(object):

    def __init__(self):
        self.s1 = []  # стек для добавления
        self.s2 = []  # стек для извлечения

    def push(self, x):
        self.s1.append(x)  # просто кладём в первый стек

    def pop(self):
        self.peek()  # убеждаемся, что s2 не пустой
        return self.s2.pop()  # извлекаем из второго стека

    def peek(self):
        # если второй стек пуст — переносим элементы
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())  # переворачиваем порядок
        return self.s2[-1]  # верхний элемент = первый добавленный

    def empty(self):
        return not self.s1 and not self.s2