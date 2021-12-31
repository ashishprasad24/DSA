from functools import cmp_to_key

class Solution:  
    
    #comparator function used in sorting the list of pairs 
    #according to increasing order of the finish time.
    def compare(self,a,b) :
        if a[0][1]!=b[0][1] :
            return a[0][1]-b[0][1]
        
        return a[1]-b[1]
    
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        
        x = []
        
        #pushing the pair of starting and finish time and their 
        #index as pair in another list.
        for i in range(n):
            x.append([[start[i],end[i]],i+1])
        
        #sorting the list.
        x = sorted(x, key=cmp_to_key(self.compare))
        last = 0
        res = 0
        
        for i in range(n) :
            
            #if the start time of this meeting is greater than or equal
            #to the finish time of previously selected meeting then 
            #we increment the counter and update last.
            if x[i][0][0] > last :
                res += 1
                last = x[i][0][1]
        
        #returning the counter.
        return res
      
