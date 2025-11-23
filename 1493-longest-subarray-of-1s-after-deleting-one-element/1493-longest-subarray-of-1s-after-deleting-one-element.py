class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0 
        k=1
        max_win=0
        zeroes=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeroes=zeroes+1

            while zeroes>k:
                if nums[l]==0:
                    zeroes=zeroes-1

                l=l+1
            max_win=max(max_win,(r-l+1))
        return max_win -1