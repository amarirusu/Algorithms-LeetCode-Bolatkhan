class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # конец нормальных элементов nums1
        j = n - 1  # конец nums2
        k = m + n - 1  # самый конец nums1

        # пока есть элементы в nums2
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # берем из nums1
                i -= 1
            else:
                nums1[k] = nums2[j]  # берем из nums2
                j -= 1

            k -= 1  # двигаем назад