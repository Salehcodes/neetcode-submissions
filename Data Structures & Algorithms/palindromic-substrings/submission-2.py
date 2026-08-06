class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]

        n=len(s)
        count=0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i+1<=3 or dp[i+1][j-1]):
                    dp[i][j]=True
                    count+=1
        
        return count