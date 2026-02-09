class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # left = 0
        # right = len(s) - 1

        # while left < right:
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1

        # return True

        # s = str(x)
        # return s==s[::-1]

        # if x<0:
        #     return False

        # org = x
        # rev = 0
        # while x>0:
        #     rev = rev*10 + x%10
        #     x //= 10
        # return org == rev

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        
        return x == rev or x == rev // 10