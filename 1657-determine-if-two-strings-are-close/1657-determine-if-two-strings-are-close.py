
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1)!=set(word2):
            return False

        count1= Counter(word1)
        count2= Counter(word2)

        if sorted(count1.values())!=sorted(count2.values()):
            return False
        return True