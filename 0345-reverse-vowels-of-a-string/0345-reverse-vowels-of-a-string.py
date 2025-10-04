class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if not (s[i] == "a" or s[i] == "A" or s[i] == "e" or s[i] == "E" or 
                    s[i] == "i" or s[i] == "I" or s[i] == "o" or s[i] == "O" or 
                    s[i] == "u" or s[i] == "U"):
                i += 1
                continue

            if not (s[j] == "a" or s[j] == "A" or s[j] == "e" or s[j] == "E" or 
                    s[j] == "i" or s[j] == "I" or s[j] == "o" or s[j] == "O" or 
                    s[j] == "u" or s[j] == "U"):
                j -= 1
                continue

            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)
