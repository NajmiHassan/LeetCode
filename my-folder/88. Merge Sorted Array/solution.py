class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_index = m - 1
        n_index = n - 1
        right = m + n - 1

        while n_index >= 0:
            if m_index >= 0 and nums1[m_index] > nums2[n_index]:
                nums1[right] = nums1[m_index]
                m_index -= 1
            else:
                nums1[right] = nums2[n_index]
                n_index -= 1

            right -= 1