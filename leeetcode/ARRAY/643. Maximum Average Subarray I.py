class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = sum(nums[0:k])

        n = len(nums)
        m = sums

        for i in range(1, n-k+1):
            sums = sums - nums[i - 1] + nums[k + i - 1]
            if(sums > m):
              m = sums
        return m / k
