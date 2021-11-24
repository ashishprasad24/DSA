
def wordBreak(line, dictionary):
    l = len(line)
    d = set(dictionary)
    dp = [False]*(l+1)
    
    def solve(line,i,d):
        if i==0:
            return True
        if dp[i]:
            return dp[i]
        
        for j in range(1,l+1):
            if line[0:j] in d and solve(line[j:i],i-j,d):
                dp[i] = True
                break 
        return dp[i]
    
    return solve(line,l,d)
