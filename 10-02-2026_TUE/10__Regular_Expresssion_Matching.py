class Solution:
    def isMatch(self, s: str, p: str) -> bool:
     
        # def dfs(i, j):
        #     if j == len(p):
        #         return i == len(s)
            
        #     first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
        #     if j + 1 < len(p) and p[j+1] == '*':
        #         return (
        #             dfs(i, j+2) or
        #             (first_match and dfs(i+1, j))
        #         )
            
        #     return first_match and dfs(i+1, j+1)
        
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] |= dp[i-1][j]
        
        return dp[m][n]