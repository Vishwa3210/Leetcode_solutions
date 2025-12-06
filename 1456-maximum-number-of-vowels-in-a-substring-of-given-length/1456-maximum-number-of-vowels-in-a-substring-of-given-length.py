class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        count=0
        max_count=0
        
        v=['a','e','i','o','u']
        if n<k:
            return 0
        for i in range(k):    
            if s[i] in v:
                count=count+1

        max_count = count
        for i in range(k,len(s)):
            if s[i] in v:
                count=count+1

            if s[i-k] in v:
                count=count-1
                
            max_count=max(max_count,count)
        return max_count
            

        