import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        # добавляем начальные элементы
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val):
        # добавляем новое значение
        heapq.heappush(self.heap, val)

        # если элементов больше k — удаляем минимальный
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # вершина кучи — k-ый по величине элемент
        return self.heap[0]