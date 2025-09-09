class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max=candies[0]
        res=[]
        i=0
        j=1
        for i in range(len(candies)):
           if candies[i]>max:
             max=candies[i]
        

        for j in range(len(candies)):
            if (candies[j]+extraCandies) >= max:
                res.append(True)

            else:
                res.append(False)

        return res

