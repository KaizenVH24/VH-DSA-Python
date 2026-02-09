class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        rev = 0

        # rev = int(str(x)[::-1]) * sign

        while x != 0:
            pop = x % 10
            x //= 10
            rev = rev*10 + pop
        rev *= sign

        if rev < -2**31 or rev > 2**31-1:
            return 0
        return rev
