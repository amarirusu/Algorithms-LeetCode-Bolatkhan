class Solution:
    def nextGreatestLetter(self, letters, target):
        for ch in letters:  # проходим по всем буквам
            if ch > target:
                return ch  # нашли первую больше

        return letters[0]  # если не нашли, возвращаем первую