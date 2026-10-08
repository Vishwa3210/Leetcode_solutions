class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ng={}
        stack=[]
        for i in nums2:
            while len(stack)!=0 and stack[-1]<i:
                ng[stack.pop()]=i

            stack.append(i)
        res=[]
        for i in nums1:
            res.append(ng.get(i,-1))

        return res

