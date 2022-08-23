/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    //naive solution
    let point=1, count = 0, it = 0;
    
    while(k>0){
        if(arr[it]!=point){
            count++;
        }else{
            it++;
        }
        if(count==k){
            return point;
        }
        point++;
    }

};