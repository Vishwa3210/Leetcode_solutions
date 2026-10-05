class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for c in s:
            if c.isalnum():
                s1=s1+c.lower()

        l=0
        r=len(s1)-1
        while l<=r:
            if s1[l] == s1[r]:
                l=l+1
                r=r-1
                
            
                
            else:
               
               return False
               
        return True

