
class Solution:
    def maxProfit(self, K, N, A):
        if not A : return 0
        N= len(A)
        dp=[0]*N
        
        for t in range(K):
            pos=(-A[0])
            profit=0
            
            for i in range(1,N):
                pos=max(pos,dp[i]-A[i])
                profit=max(profit,pos+A[i])
                dp[i]=profit
                
        return dp[-1]        
        
