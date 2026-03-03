class Solution:
  def findLargest(self, arr):
    arr = list(map(str, arr))  # converting all string to integer
    
    # custom comparator
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y  < y + x:
            return 1
        else:
            return 0
            
   # Sort using custom comparator
        arr.sort(key=cmp_to_key(compare))
   
    # Edge case: if the largest number is 0, return "0."
        if arr[0] == "0":
            return "0"
        
        # Join and return result
        return "".join(arr)