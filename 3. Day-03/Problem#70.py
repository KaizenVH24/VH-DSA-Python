# Brute Force (Recursive)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
# TC = (2**n)

# Optimized
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# TC & SC = O(n)

#Space optimized
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        prev2 = 1
        prev1 = 1

        for i in range(2,n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1
 
# SC = O(1)