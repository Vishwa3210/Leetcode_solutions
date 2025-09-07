class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        expected = "a"   
        
        for ch in word:
            while ch != expected:  
                ans += 1
                if expected == "a":
                    expected = "b"
                elif expected == "b":
                    expected = "c"
                else:
                    expected = "a"
            
            if expected == "a":
                expected = "b"
            elif expected == "b":
                expected = "c"
            else:
                expected = "a"
        
        if expected == "b":
            ans += 2  
        elif expected == "c":
            ans += 1   
        
        return ans
