#User function Template for python3
def kth(arr1,arr2,s1,e1,s2,e2,k):
    if s1==e1 :
        return arr2[s2+k]
    if s2==e2 :
        return arr1[s1+k]

    m1 = (e1 -s1)//2
    m2 = (e2-s2)//2
    if m1+m2 < k :
        if arr1[s1+m1] > arr2[s2+m2]:
            return kth(arr1, arr2, s1, e1, s2 + m2 + 1, e2, k - m2 - 1)
        else :
            return kth(arr1, arr2, s1 + m1 + 1, e1, s2, e2, k - m1 - 1)

    else :
        if arr1[s1 + m1] > arr2[s2 + m2] :
            return kth(arr1, arr2, s1, s1 + m1, s2, e2, k)
        else:
            return kth(arr1, arr2, s1, e1, s2, s2 + m2, k)
                
class Solution:

    def kthElement(self,arr1,arr2,n,m,k):
        return kth(arr1, arr2, 0, n, 0, m,k-1)
