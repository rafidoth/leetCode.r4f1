/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    
    return function(n) {
       let start = 1, end = n;
        while(start<=end){
            let mid = Math.floor((start+end)/2);
            if(isBadVersion(mid)==true && isBadVersion(mid-1)==false){
                return mid;
            }
            if(isBadVersion(mid)==true && isBadVersion(mid-1)==true){
                end = mid-1;
            }
            if(isBadVersion(mid)!=true){
                start = mid+1;
            }
        
       }
     
    };
};