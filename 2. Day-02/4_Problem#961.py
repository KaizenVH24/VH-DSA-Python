"""
Input = [1,2,3,3]
Output = 3 [repeated value]

=============================================
Link - https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/
=============================================
"""

#Solution-1
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        h = set()

        for i in nums:
            if i in h:
                return i
            h.add(i)


#Solution-2
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == nums[i-1] or nums[i] == nums[i-2]:
                return nums[i]