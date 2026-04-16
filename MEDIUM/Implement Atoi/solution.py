
class Solution:
    def myAtoi(self, s):
        #Sam
        def checkNum(num):
            try:
                float(num)
                return True
            except ValueError:
                return False
        s = s.strip()
        if not s:
            return 0
        i = 0
        sign = 1
        if s[0]=='-' or s[0]=='+':
            sign = -1 if s[0]=='-' else 1
            i += 1
        
        result = 0
        isNum = True
        for j in range(i,len(s)):
            if checkNum(s[j]) and isNum:
                result *=10
                result += int(s[j])
            else:
                isNum = False
                # print(s[j])   
        result *= sign
        int_min, int_max = -2**31, 2**31 - 1
        if sign==-1 and result<int_min:
            return int_min
        if sign==1 and result>int_max:
            return int_max
        return result