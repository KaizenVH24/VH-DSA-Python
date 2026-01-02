"""
input = [1,2,3,4]
output = [24,12,8,6]

=========================================
Link - https://leetcode.com/problems/product-of-array-except-self/description/
=========================================
"""

#Solution-1 (TC & SC = o(n))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_multiply = 1
        right_multiply = 1
        n = len(nums)
        left_arr = [0]*n
        right_arr = [0]*n

        for i in range(n):
            j = -i-1
            left_arr[i] = left_multiply
            right_arr[j] = right_multiply

            left_multiply *= nums[i]
            right_multiply *= nums[j]

        return [l*r for l,r in zip(left_arr, right_arr)]
    

#SOlution-2 (SC - O(1))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer