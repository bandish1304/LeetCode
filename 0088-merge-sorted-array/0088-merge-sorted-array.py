class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums1.append(nums1[i])
                i = i+1
            else:
                nums1.append(nums2[j])
                j = j + 1
        while j < n:
            nums1.append(nums2[j])
            j = j+ 1
        while i < m:
            nums1.append(nums1[i])
            i = i+1
        i = 0
        j = 0
        while i < len(nums1):
            nums1.pop(j)
            i += 1