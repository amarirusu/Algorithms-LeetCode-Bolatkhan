class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1 #левый правый индекс

        while left <= right: # пока они не пересиклись
            mid = (left + right) // 2 #середину ищем

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return left