/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    let start =0;
    let end = arr.length
    while(start<=end){
        let mid = Math.floor((start+end)/2);
        if(arr[mid]>arr[mid+1]){
            if(arr[mid]>arr[mid-1]){
                return mid;
            }
            else{
                end = mid -1;
            }
        }else{
            start = mid+1
        }
    }
};