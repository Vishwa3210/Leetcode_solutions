class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        res=nums[0]
        for j in range(len(nums)):
            if total<0:
                total= 0

            
            total=total+nums[j]
            res=max(total,res)
            j=j+1

        return res

        