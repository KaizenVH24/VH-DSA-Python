class Solution:
    def myAtoi(self, s: str) -> int:
        # s = s.lstrip()
        # if not s:
        #     return 0
        
        # sign = 1
        # i = 0
        
        # if s[0] == '-':
        #     sign = -1
        #     i += 1
        # elif s[0] == '+':
        #     i += 1
        
        # num = 0
        # while i < len(s) and s[i].isdigit():
        #     num = num * 10 + int(s[i])
        #     i += 1
        
        # num *= sign
        
        # if num < -2**31:
        #     return -2**31
        # if num > 2**31 - 1:
        #     return 2**31 - 1
        
        # return num

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num