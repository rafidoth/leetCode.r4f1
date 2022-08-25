/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let start = 0, end = nums.length-1;
    while(start<=end){
        let mid = Math.floor((start+end)/2);
        if(nums[mid]>target){
            end = mid -1;
        }
        else if(nums[mid]==target){
            return mid
        }
        else{
            start = mid +1 ;
        }
    }
    return (end+1);
};