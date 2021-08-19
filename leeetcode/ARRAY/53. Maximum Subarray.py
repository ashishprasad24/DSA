class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum,currsum = float('-inf'),0
        
        for n in nums:
            currsum = max(currsum+n,n)
            maxsum= max(maxsum,currsum)
            
        return maxsum    
        
