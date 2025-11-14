class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i=j=float('inf')
        for x in nums:
            if x<=i:
                i=x
            elif x<=j:
                j=x

            else:
                return True
        return False