class Solution:
    def magicalString(self, n: int) -> int:
        s='122'
        if n<=1:
            return 1
        i=2
        num=1
        while len(s)<n:
            count = int(s[i])
            s+=str(num)*count
            num=3-num
            i+=1
        return s[:n].count('1')
