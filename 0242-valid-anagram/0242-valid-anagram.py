class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter={}
    
        if len(s)!=len(t):
            return False

        for i in s:
            if i in counter:
                counter[i]=counter.get(i)+1
            else:
                counter[i]=1
            

        for i in t:
            if i not in counter or counter[i]==0:
                return False

            counter[i]=counter[i]-1

        return True