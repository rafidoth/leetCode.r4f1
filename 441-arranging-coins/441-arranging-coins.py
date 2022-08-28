class Solution:
    def arrangeCoins(self, n: int) -> int:
        start =1
        end = n
        while(start<=end):
            mid = (start+end)//2
            s = mid*(mid+1)/2
            if(s==n):
                return mid
            elif(s>n):
                end = mid -1
            else:
                start = mid +1
        return end