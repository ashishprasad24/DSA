
class Solution:
    #Function to merge two sorted list into one sorted list.
    def MergeLists(self,n1,n2):
        ret = None
        
        #comparing data in both lists and storing the smaller in result and
        #recursively calling the MergeLists function for next node in result.
        if n2.data<n1.data:
            ret=n2
            n2=n2.next
        else:
            ret=n1
            n1=n1.next
        
        tail=ret
        
        while n1 is not None and n2 is not None:
            if n2.data<n1.data:
                tail.next=n2
                tail=n2
                n2=n2.next
            else:
                tail.next=n1
                tail=n1
                n1=n1.next
                
        if n1:
            tail.next=n1
        if n2:
            tail.next=n2
        
        #returning the resultant list.
        return ret
    
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        N = K
        last = N-1
        
        while last != 0:
            i = 0
            j = last
            while i<j:
                #calling MergeLists function to merge two different list into
    			#one list which has sorted elements.
                arr[i] = self.MergeLists(arr[i], arr[j])
                
                #going for the next pair of lists.
                i+=1
                j-=1
                
                #if all pairs are merged, we update the last.
                if (i >= j):
                    last = j
                    
        #returning the merged list.            
        return arr[0]
