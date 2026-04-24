class Solution:
    def visibleBuildings(self, arr):
        # code here
        count = 0
        max_height = 0
        
        for height in arr:
            if (height > max_height or height == max_height):
                count += 1
                max_height = height
        
        return count
