# TC = O(n**2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
    

# TC - O(nlogn)
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for i in nums:
            idx = bisect.bisect_left(tails, i)

            if idx == len(tails):
                tails.append(i)
            else:
                tails[idx] = i

        return len(tails)