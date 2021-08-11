class Solution:
     def maxProfit(self, prices):
      """
      :type prices: List[int]
      :rtype: int
      """
      if not prices:
         return 0
      leftMin,rightMax = [0 for i in range(len(prices))],[0 for i in range(len(prices))]
      leftMin[0] = prices[0]
      for i in range(1,len(prices)):
         leftMin[i] = min(leftMin[i-1],prices[i])
      #print(leftMin)
      rightMax[-1]= prices[-1]
      for i in range(len(prices)-2,-1,-1):
         rightMax[i] = max(rightMax[i+1],prices[i])
      #print(rightMax)
      ans = 0
      for i in range(len(prices)-1):
         ans = max(ans,rightMax[i+1]-leftMin[i])
      return ans
ob1 = Solution()
print(ob1.maxProfit([7,2,5,8,6,3,1,4,5,4,7]))
