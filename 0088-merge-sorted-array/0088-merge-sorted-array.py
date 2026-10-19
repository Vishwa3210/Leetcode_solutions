class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        for num in range(m+n-1,-1,-1):
            if j<0:
                break

            else:
                if i>0 and nums1[i]>nums2[j]:
                    nums1[num]=nums1[i]
                    i-=1
                   

                else: 
                    nums1[num]=nums2[j]
                        
                    j-=1        

            

        return nums1.sort()

