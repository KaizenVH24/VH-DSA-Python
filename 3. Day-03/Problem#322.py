#Brute Force - Recursive

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        if amount < 0:
            return float('inf')

        ans = float('inf')
        for i in coins:
            res = self.coinChange(coins, amount-i)
            ans = min(ans, res+1)
        
        return ans
    
# Optimized

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c]+1)

        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1