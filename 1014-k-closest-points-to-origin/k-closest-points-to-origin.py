import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            # считаем квадрат расстояния до начала координат
            dist = x * x + y * y

            # используем max-heap через отрицательное расстояние
            heapq.heappush(heap, (-dist, x, y))

            # если в куче больше k элементов удаляем самый дальний
            if len(heap) > k:
                heapq.heappop(heap)

        # возвращаем точки без расстояний
        return [[x, y] for dist, x, y in heap]