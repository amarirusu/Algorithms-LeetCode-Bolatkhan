class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums  # если 1 элемент

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])   # делим левую часть
        right = self.sortArray(nums[mid:])  # делим правую часть

        return self.merge(left, right)  # соединяем

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        # сравниваем элементы
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # добавляем остатки
        result += left[i:]
        result += right[j:]

        return result