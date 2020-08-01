class Solution:
    def numDecodings(self, s: str) -> int:        
        # 思路：这是一个含有多个条件的特殊爬楼梯问题。因为在+1个字母 & +2个字母都有特殊情况，所以dp方程要在
        # 爬楼梯的dp方程中分段来写
        # dp方程：
        # 1.dp[i+1] = 0. if s[i] == '0' and (s[i-1:i+1] < '10' or s[i-1:i+1]>'26')
        # 2.dp[i+1] = dp[i]. if s[i]!= '0' and (s[i-1:i+1] < '10' or s[i-1:i+1]>'26')
        # 3.dp[i+1] = dp[i-1]. if s[i] == '0' and (s[i-1:i+1] >= '10' and s[i-1:i+1]<='26')
        # dp[i+1] = dp[i]+dp[i-1]. if s[i] != '0' and (s[i-1:i+1] >= '10' and s[i-1:i+1]<='26')
    
        n = len(s)
        if n==0: return 0
        dp = [1,0]
        dp[1] = 1 if s[0]!='0' else 0 
        for i in range(1,n):
            dp.append(0)
            if s[i]!='0':
                dp[i+1] += dp[i]
            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26':
                dp[i+1] += dp[i-1]
        
        return dp[-1]