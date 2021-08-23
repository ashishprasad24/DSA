class Solution(object):
       def search(self, nums, target):
        def recur_search(nums,target,left,right):
            if left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return recur_search(nums,target,mid+1,right)
                else:
                    return recur_search(nums,target,left,mid-1)
            else: return -1
        
        left,right = 0, len(nums)-1
        return recur_search(nums,target,left,right)  
        
