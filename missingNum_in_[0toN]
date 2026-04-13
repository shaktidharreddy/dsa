class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s = sum(nums)

        n = max(nums)
        t = int(n*(n+1)/2)

        missing_num = t -s

        if missing_num ==0 and min(nums)==0 :
            return n+1 
        else:
            return missing_num

        
