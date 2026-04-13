class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        res = num[:]
        
        # Step 1: mirror left → right
        i, j = 0, n - 1
        while i < j:
            res[j] = res[i]
            i += 1
            j -= 1
        
        # Step 2: if mirrored > original → return
        if res > num:
            return res
        
        # Step 3: add 1 to middle
        carry = 1
        mid = (n - 1) // 2
        
        i = mid
        j = mid if n % 2 == 1 else mid + 1
        
        while i >= 0 and carry:
            val = res[i] + carry
            res[i] = val % 10
            res[j] = res[i]
            carry = val // 10
            i -= 1
            j += 1
        
        # Step 4: all 9s case
        if carry:
            return [1] + [0] * (n - 1) + [1]
        
        return res