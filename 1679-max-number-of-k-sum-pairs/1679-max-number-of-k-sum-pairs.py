class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res= 0
        l=0
        r=len(nums)-1
        
        while l<r:
            sum1=nums[l]+nums[r]
            if sum1==k:
                res=res+1
                l=l+1
                r=r-1

            elif sum1<k:
                l=l+1
            else:
                r=r-1

        return res