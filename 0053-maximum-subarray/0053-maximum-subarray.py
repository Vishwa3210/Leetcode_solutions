class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        res=nums[0]
        for i in range(len(nums)):
            if total<0:
                total=0

            total=total+nums[i]
            res=max(total,res)
            i=i+1

        return res
        