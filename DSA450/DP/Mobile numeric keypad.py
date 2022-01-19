class Solution:
    def solve(self, i, j, n):
        if n == 1: return 1
        
        if self.dp[self.keypad[i][j]][n] != -1: return self.dp[self.keypad[i][j]][n]
        
        a = self.solve(i, j, n - 1)
        # b = c = d = e = 0
        
        if j - 1 >= 0 and self.keypad[i][j - 1] != -1:
                a += self.solve(i, j - 1, n - 1)
        
        if j + 1 < 3 and self.keypad[i][j + 1] != -1:
                a += self.solve(i, j + 1, n - 1)
        
        if i- 1 >= 0 and self.keypad[i - 1][j] != -1:
                a += self.solve(i - 1, j, n - 1)
        
        if i + 1 < 4 and self.keypad[i + 1][j] != -1:
                a += self.solve(i + 1, j, n - 1)
        
        self.dp[self.keypad[i][j]][n] = a
        return a
        
    
    def getCount(self, n):
        self.keypad = [[1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [-1,0,-1]]

        # dp[i][j] => count for ith keypad with j length
        self.dp = [[-1 for _ in range(n + 1)] for _ in range(10)]
        ans = 0
        for i in range(4):
            for j in range(3):
                if self.keypad[i][j] != -1:
                    ans += self.solve(i, j, n)
        return ans
