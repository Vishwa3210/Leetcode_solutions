class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        i=0
        
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1

            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total>0:
                    k=k-1

                elif total<0:
                    j=j+1

                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1

                    while j<k and nums[j]==nums[j-1] :
                        j=j+1

        return res
