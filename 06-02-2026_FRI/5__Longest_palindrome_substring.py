class Solution:
    def longestPalindrome(self, s: str) -> str:
        # n = len(s)
        # longest = ""

        # for i in range(n):
        #     for j in range(i,n):
        #         sub = s[i:j+1]
        #         if sub == sub[::-1]:
        #             if len(sub) > len(longest):
        #                 longest = sub
        # return longest

        res = ""

        def expand(l,r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)

            res = max(res, odd, even, key=len)
        return res