# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # if not strs:
        #     return ""
        
        # prefix = strs[0]
        
        # for s in strs[1:]:
        #     i = 0
        #     while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
        #         i += 1
        #     prefix = prefix[:i]
            
        #     if prefix == "":
        #         return ""
        
        # return prefix

        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        
        return strs[0]

# ---------------------------------------------------------------------------------------------

# 15. 3Sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

# ---------------------------------------------------------------------------------------------

# 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        
        return closest

  # Vinay Hulsurkar aka VH24
