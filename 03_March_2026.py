# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        mapping = {
            '2': "abc", '3': "def", '4': "ghi",
            '5': "jkl", '6': "mno", '7': "pqrs",
            '8': "tuv", '9': "wxyz"
        }
        
        result = [""]
        
        for digit in digits:
            temp = []
            for combo in result:
                for letter in mapping[digit]:
                    temp.append(combo + letter)
            result = temp
        
        return result
# Time: O(4^n * n)
# Space: O(4^n)

# -----------------------------------------------------------------------------------

# 18. 4Sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

  # Time: O(n³)
  # Space: O(1) (excluding output)

# Vinay Hulsurkar aka VH24
