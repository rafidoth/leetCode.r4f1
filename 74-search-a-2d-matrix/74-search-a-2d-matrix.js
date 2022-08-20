/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let r_len = matrix.length;
    let c_len = matrix[0].length;
    
    let start = 0;
    let end = r_len*c_len -1;
    
    while(start <= end){
        let mid = Math.floor((start+end)/2);
        let r = Math.floor(mid/c_len) ;
        let c = mid % c_len;
        if(matrix[r][c]==target){
            return true
        }
        else if(matrix[r][c]>target){
            end = mid -1
        }
        else{
            start = mid +1
        }
    }
    return false
};