class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x//2
        while(start<=end):
            mid = (start+end)//2
            sqr = mid*mid
            if(sqr==x) :
                return mid
            if(sqr<x):
                start = mid+1
            if(sqr>x):
                end = mid -1
        if x== 1:
            return 1
        else :
            return end