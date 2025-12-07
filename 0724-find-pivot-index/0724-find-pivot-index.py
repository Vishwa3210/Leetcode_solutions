class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total=sum(nums)
        leftSum=0
        for i in range(n):
            rightSum=total -leftSum -nums[i]
            if leftSum==rightSum:
                return i

            leftSum=leftSum+nums[i]
        return -1

