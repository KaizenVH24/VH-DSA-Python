# Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            width = r - l
            h = min(height[l], height[r])
            area = width * h
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
# --------------------------------------------------------------------------------------------------------------#

# Integer To Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        # thousands = ["", "M", "MM", "MMM"]
        # hundreds = ["", "C", "CC", "CCC", "CD", "D",
        #             "DC", "DCC", "DCCC", "CM"]
        # tens = ["", "X", "XX", "XXX", "XL", "L",
        #         "LX", "LXX", "LXXX", "XC"]
        # ones = ["", "I", "II", "III", "IV", "V",
        #         "VI", "VII", "VIII", "IX"]
        
        # return (
        #     thousands[num // 1000] +
        #     hundreds[(num % 1000) // 100] +
        #     tens[(num % 100) // 10] +
        #     ones[num % 10]
        # )

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        result = ""
        
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        
        return result
# --------------------------------------------------------------------------------------------------------------#
      
# Roman To Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        
        return total
# Vinay Hulsurkar aka VH24
