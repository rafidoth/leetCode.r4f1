class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occ = self.binarySearch(nums, target, True)
        second_occ = self.binarySearch(nums, target, False)
        return [first_occ, second_occ]
    
    #search direction: true-> left   false->right
    
    def binarySearch(self, nums, target, searchDirection):
        start = 0
        end = len(nums)-1
        result = -1
        while(start<=end):
            mid = (start+end)//2
            temp = nums[mid]
            if(temp>target):
                end = mid -1
            elif(temp<target):
                start = mid +1
            else:
                result = mid
                if(searchDirection):
                    end = mid -1
                else:
                    start = mid+1
        return result      