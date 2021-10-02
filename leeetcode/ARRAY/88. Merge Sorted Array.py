class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from end of both arrays
        while m > 0 and n > 0:
            # looking at elements in the back
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        # account for remaining nums2 integers
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1
