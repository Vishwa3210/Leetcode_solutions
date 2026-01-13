class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for nums in arr:
            if nums in freq:
                freq[nums]=freq[nums]+1
            else:
                freq[nums]=1

        seen=set()
        for count in freq.values():
                if count in seen:
                    return False
                seen.add(count)
                
        return True