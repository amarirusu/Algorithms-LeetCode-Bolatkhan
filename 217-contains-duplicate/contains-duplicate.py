class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()  # хэш-таблица (множество)
        for num in nums:
            if num in seen:  # поиск за O(1)
                return True
            seen.add(num)   # вставка за O(1)
        return False