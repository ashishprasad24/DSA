class Solution{
  public:
    int missingNumber(vector<int>& array, int n) {
        
        int sum=0;
        sum= n*(n+1)*(0.5);
        
        int asum=0;
        for(int i=0; i<n-1;i++){
        asum +=array[i];
        
        
        }
        
        return sum-asum;
        
    }
};
