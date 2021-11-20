class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r,N=matrix[0][0],matrix[-1][-1],len(matrix)
        
        def lessk(m):
            cnt=0
            for r in range(N):
                x=bisect_right(matrix[r],m)
                cnt+=x
            return cnt
        
        while l<r:
            mid = (l+r)//2
            if lessk(mid)<k:
                l=mid+1
            else:
                r=mid
        return l        
        
