class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res , count=0,0
        
        for n in nums:
            if count == 0:
                res= n
            count += (1 if n== res else -1) 
            
            count={}
            res,maxcount=0,0
            
            for n in nums:
                count[n]=1 + count.get(n,0)
                res=n if count[n]>maxcount else res
                maxcount = max(count[n],maxcount)
            return res    
        
        
