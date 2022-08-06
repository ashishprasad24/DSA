class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i=0
        while i < len(arr)-1:
          if arr[i]==0:
            insert.arr(i+1,0)
            del arr[len(arr)-1]
            i+=2
        else:
          i+=1
