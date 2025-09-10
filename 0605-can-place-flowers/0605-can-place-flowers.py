class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res=0
        x=len(flowerbed)
        for i in range(x):
            if flowerbed[i]==0:
                left=(i==0 or flowerbed[i-1]==0)
                right=(i==(x-1) or flowerbed[i+1]==0)

                if left and right:
                    flowerbed[i]=1
                    res=res+1
                    i=i+1

        if res>=n:
            return(True)

        else:
            return(False)

            
