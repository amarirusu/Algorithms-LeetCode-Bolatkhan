class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            nado = target - num
            if nado in seen:
                return [seen[nado], i]
            seen[num] = i
