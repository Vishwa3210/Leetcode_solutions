class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                if nums[low]==target and nums[high]==target:
                    return[low,high]
                if nums[low]!=target:
                    low=low+1
                    
                if nums[high]!=target:
                    high=high-1

        return[-1,-1]
            