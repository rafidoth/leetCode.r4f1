class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        while(True):
            n=n-i
            i=i+1
            if(n==0):
                return i-1
            if(n<0):
                return i-2