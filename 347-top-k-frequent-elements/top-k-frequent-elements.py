import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        
        # считаем сколько раз встречается каждый элемент
        count = Counter(nums)
        
        heap = []
        
        # добавляем в кучу пары частота и число
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            
            # если размер больше k  удаляем элемент с наименьшей частотой
            if len(heap) > k:
                heapq.heappop(heap)
        
        # возвращаем только числа
        return [num for freq, num in heap]