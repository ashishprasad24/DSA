
class Solution:
    
    #Function to check if current minimum value is feasible or not.
    def isPossible(self,arr, n, m, curr_min): 
        
        studentsRequired = 1
        curr_sum = 0
      
        #iterating over all the books.
        for i in range(n): 
    
            #if current number of pages are greater than curMin, return false
            if (arr[i] > curr_min): 
                return False
      
            #counting number of students required to distribute curMin pages
            if (curr_sum + arr[i] > curr_min): 
                
                #incrementing student count and updating curSum.
                studentsRequired += 1
                curr_sum = arr[i] 
      
                #if students required becomes greater than given number 
                #of students, we return false.
                if (studentsRequired > m): 
                    return False
                    
            #else updating curSum
            else: 
                curr_sum += arr[i] 
      
        return True
    
    #Function to find minimum number of pages. 
    def findPages(self,arr, n, m): 
    
        sum = 0
        #returning -1 if no. of books is less than no. of students.
        if (n < m): 
            return -1
      
        for i in range(n): 
            sum += arr[i]
            
        #initializing start as 0 pages and end as total pages.
        start, end = 0, sum
        result = 10**9
      
        while (start <= end): 
      
            mid = (start + end) // 2
            
            #checking if it is possible to distribute books 
            #by using mid as current minimum.
            if (self.isPossible(arr, n, m, mid)): 
                
                #if yes, then we find the minimum distribution.
                result = min(result, mid) 
                
                #as we are finding minimum and books are sorted 
                #so reducing end as end = mid -1.
                end = mid - 1
                
            #if not possible means pages should be increased so
            #updating start = mid + 1.
            else: 
                start = mid + 1
      
        #returning minimum number of pages.
        if result== 10**9:
            return -1
        else:
            return result
            
            
