class Solution {
public:
    int climbStairs(int n) {
        if(n<=1)
        return 1;

        return climbStairs(n-2)+climbStairs(n-1);
        

        
    }
};
