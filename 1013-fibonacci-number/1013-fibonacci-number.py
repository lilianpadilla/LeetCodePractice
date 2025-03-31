class Solution:
    def fib(self, n: int) -> int:
        dp = []
        if n < 2:
            return n
            
        dp.append(0)
        dp.append(1)

        for i in range(2,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[-1]
