class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            if (nums[i]+1)%3==0 or (nums[i]-1)%3 ==0:
                count=count+1
                i=i+1

            elif (nums[i])%3==0 :
            
                i=i+1

            

        return count

            
    

    