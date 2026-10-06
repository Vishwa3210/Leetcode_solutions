class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter={}
        left=0
        count=0
        for r in range(len(s)):
            if s[r] in counter:
                left=max(left,counter[s[r]]+1)

            counter[s[r]]=r
            count=max(count,r-left+1)
        return count