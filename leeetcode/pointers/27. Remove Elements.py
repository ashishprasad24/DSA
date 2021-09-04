class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # approach: two pointers i and j
        #     elements before and included i are not equal to val
        #     iterate list by j, once element in j is not equal val, save it and move i ahead

        i = -1
        for j in range(len(nums)):
            if nums[j] != val:
                i = i + 1
                nums[i] = nums[j]
        return i + 1
