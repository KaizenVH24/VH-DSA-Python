"""
[2,7,11,19]   target = 9
nums[0] + nums[1] = target

result = [0,1]

==================================================
Link - https://leetcode.com/problems/two-sum/
==================================================
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, v in enumerate(nums):
            complement = target - v
            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[v] = i