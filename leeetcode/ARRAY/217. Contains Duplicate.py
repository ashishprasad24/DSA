class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        
        if len(s)==len(nums):
            return False
        else:
            return True
        
