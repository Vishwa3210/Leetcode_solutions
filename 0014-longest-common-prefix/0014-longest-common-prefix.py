class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        res=""
        if len(strs)==0:
            return ""

        base=strs[0]
        for i in range(0,len(base)):
            for word in strs[1:]:
                if i==len(word) or word[i]!=base[i]:
                    return res

            res=res+base[i]

        return res