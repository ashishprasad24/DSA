 
# Function to return k'th smallest
# element in a given array
def kthSmallest(arr, n, k):
 
    # Sort the given array
    arr.sort()
 
    # Return k'th element in the
    # sorted array
    return arr[k-1]
