class Solution:
    def sortArray(self, nums):
        # Базовый случай: список из 1 элемента уже отсортирован
        if len(nums) <= 1:
            return nums

        # Разделяем массив пополам
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Сливаем две половины в одну отсортированную
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        
        # Сравниваем элементы из двух списков
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Добавляем остатки
        result.extend(left[i:])
        result.extend(right[j:])
        return result