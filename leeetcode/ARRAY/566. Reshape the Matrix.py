class Solution:
    def matrixReshape(self, nums, r, c):
        m, n, count = len(nums), len(nums[0]), 0
        if m*n != r*c: return nums
        res = [[0] * c for _ in range(r)]
        for i, j in product(range(m), range(n)):
            res[count//c][count%c] = nums[i][j]
            count += 1      
        return res
        
