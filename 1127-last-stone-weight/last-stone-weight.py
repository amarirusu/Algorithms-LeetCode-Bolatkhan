class Solution(object):
    def lastStoneWeight(self, stones):
        # делаем max-heap, используя отрицательные значения
        heap = [-s for s in stones]
        heapq.heapify(heap)

        # пока есть минимум два камня
        while len(heap) > 1:
            y = -heapq.heappop(heap)  # самый тяжёлый
            x = -heapq.heappop(heap)  # второй по тяжести

            if y != x:
                # добавляем разницу обратно в кучу
                heapq.heappush(heap, -(y - x))

        # если камень остался — возвращаем его вес, иначе 0
        return -heap[0] if heap else 0