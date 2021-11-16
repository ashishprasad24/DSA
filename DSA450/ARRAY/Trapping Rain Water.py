class Solution:
    def trappingWater(self, arr,n):
        
        if not arr: return 0
        l,r=0,len(arr)-1
        leftmax,rightmax = arr[l],arr[r]
        res=0
        
        while l<r:
            if leftmax <rightmax:
                l+=1
                leftmax = max (leftmax,arr[l])
                res +=leftmax - arr[l]
            else:
                r-=1
                rightmax= max(rightmax,arr[r])
                res += rightmax - arr[r]
        return res       
        
