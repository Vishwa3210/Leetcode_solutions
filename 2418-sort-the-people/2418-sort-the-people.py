class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n= len(heights)
        for i in range(n):
            for j in range(n-1):
                if heights[j]<heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
                    names[j],names[j+1]=names[j+1],names[j]

        return names
        
        

