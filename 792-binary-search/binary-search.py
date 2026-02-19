class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1  # левый и правый индекс

        while left <= right:  # пока не пересеклись
            mid = (left + right) // 2  # середина

            if nums[mid] == target:
                return mid  # вернем индекс

            if nums[mid] < target:
                left = mid + 1  # число справа
            else:
                right = mid - 1  # число слева

        return -1  # если не нашли по новой