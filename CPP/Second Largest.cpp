class Solution{
public:	
	// Function returns the second
	// largest elements
	int print2largest(int arr[], int n) {
	    int ans= -1;
	    for(int i=0; i<n; i++){
	        if(arr[i]>ans)
	            ans=arr[i];
	        
	    }
	    
	    int second=-1;
	    for(int i=0; i<n; i++){
	        if(arr[i] !=ans)
	        second= max(second,arr[i]);
	    }
	    return second;
	   
	}  
	
};
