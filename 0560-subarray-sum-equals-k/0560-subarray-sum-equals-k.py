class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numsMap={0:1}
        i=0
        current_sum=0
        count=0
        minus=0

        for i in nums:
            current_sum=current_sum+i
            minus=current_sum-k
            if minus in numsMap:
                count=count+numsMap[minus]

            numsMap[current_sum]=numsMap.get(current_sum,0)+1
        return count

       