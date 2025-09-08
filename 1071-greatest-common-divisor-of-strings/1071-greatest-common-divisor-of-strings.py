class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res=[]
        i=0
        j=0
        while i<len(str1) and j<len(str2): 
            if str1[i] == str2[j] and str1[i] not in res:
                
                res.append(str1[i])

            i=i+1
            j=j+1
        return "".join(res)