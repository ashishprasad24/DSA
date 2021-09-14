class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=0
        r=n
        
        while l<=r:
            mid=(r+l)//2
            mid_value=(mid*(mid+1))//2
            
            if mid_value == n:
                return mid
            elif mid_value< n:
                l=mid+1
            else:
                r=mid-1
        return r   
