class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        x=[[False]*(n+1) for _ in range(m+1)]
        x[0][0]=True
        for i in range(1, n+1):
            if p[i-1]=='*':
                x[0][i]=x[0][i-1]
        for i in range (1,m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':
                    x[i][j]=x[i-1][j] or x[i][j-1]
                elif p[j-1]=='?' or p[j-1]==s[i-1]:
                    x[i][j]=x[i-1][j-1]

        return x[m][n]