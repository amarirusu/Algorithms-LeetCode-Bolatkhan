class Solution:
    def climbStairs(self, n):
        # Базовые случаи
        if n <= 2:
            return n
        
        # a — dp[i-2], b — dp[i-1]
        a, b = 1, 2
        
        for i in range(3, n + 1):
            a, b = b, a + b
        
        return b