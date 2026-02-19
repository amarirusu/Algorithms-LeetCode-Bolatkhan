class Solution(object):
    def sortArray(self, nums):
        # Если в списке 1 элемент или меньше, он уже отсортирован
        if len(nums) <= 1:
            return nums
        
        # 1. Разделение: находим середину и делим массив
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # 2. Слияние: соединяем две части в одну
        return self.merge(left_half, right_half)
    
    def merge(self, left, right):
        sorted_arr = []
        i = j = 0
        
        # Сравниваем элементы из обеих половин
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        
        # Добавляем оставшиеся элементы (если они есть)
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        
        return sorted_arr