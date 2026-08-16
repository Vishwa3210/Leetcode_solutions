class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        visited=set()
        length=0
        for j in range(len(s)):
            while s[j] in visited:
                visited.remove(s[i])
                i=i+1
            visited.add(s[j])
            length=max(length,j-i+1)
        return length


        
