class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        max_profit=0
        profit=0
        while j<len(prices):
            if prices[i]<prices[j]:
                profit=prices[j]-prices[i]
                max_profit=max(profit,max_profit)
            else:
                i=j

            j=j+1
        return max_profit