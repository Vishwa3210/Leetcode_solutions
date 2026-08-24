class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=0
        y=str(x)
        j=len(y)-1
        while i<j:
            if y[i]==y[j]:
                i=i+1
                j=j-1
            else:
                return False
        return True
