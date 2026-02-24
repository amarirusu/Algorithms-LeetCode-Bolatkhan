import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            
            # если в куче больше k элементов —
            # удаляем самый маленький
            if len(heap) > k:
                heapq.heappop(heap)

        # вершина min-heap это k-ый по величине
        return heap[0]