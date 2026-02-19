class Solution:
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1  # левый и правый индекс

        while left <= right:  # пока не пересеклись
            mid = (left + right) // 2  # середина

            if letters[mid] <= target:
                left = mid + 1  # если буква меньше или равна, идем вправо
            else:
                right = mid - 1  # если больше, идем влево

        return letters[left % len(letters)]  # если вышли за границы, берем первую