class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        first=0
        second=0
        
        while first<len(word1) and second < len(word2):
            res.append(word1[first])
            res.append(word2[second])

            first=first+1
            second=second+1

        if len(word1)>len(word2):
            res.append(word1[first:])

        if len(word2)>len(word1):
            res.append(word2[second:])

        return "".join(res)


        
