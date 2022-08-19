class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start = 0
        end = len(arr)-1
        while(start<= end):
            mid = (start+end)//2
            if (arr[mid]>arr[mid+1]):
                if(arr[mid]>arr[mid-1]):
                    return mid
                else:
                    end = mid-1 
            else:
                start = mid+1
                
                    