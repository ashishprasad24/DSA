class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
            
        def twopt(arr, i, j):
            while (i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return arr
        
        if k > len(nums):
            k %= len(nums)
            
        if (k > 0):
            twopt(nums, 0, len(nums) - 1)  # rotate entire array
            twopt(nums, 0, k - 1)          # rotate array upto k elements
            twopt(nums, k, len(nums) - 1)  # rotate array from k to end of array
        
