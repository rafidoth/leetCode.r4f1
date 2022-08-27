/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
    let start =0, end = numbers.length-1;
    while(true){
        let sum= numbers[start] + numbers[end];
        if(sum>target){
            end = end -1; 
        }else if(sum == target){
            return [start+1, end+1];
        }else{
            start = start +1;
        }
    }
  };