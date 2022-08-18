class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        
        start =0 
        end = len(letters)-1
        while(start<=end):
            mid = (start+end)//2
            if(target<letters[mid]):
                end = mid-1
            else:
                start = mid+1
        return letters[start%len(letters)]
            
   
