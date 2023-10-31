class Solution{
    public:
    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    long long maxSubarraySum(int arr[], int n){
        
        long long maxi= INT_MIN, prefix=0;
        for(int i=0; i<n;i++)
        {
            prefix +=arr[i];
            maxi=max(prefix, maxi);
            if(prefix<0)
            prefix=0;
        }
        return maxi;
        
    }
};
