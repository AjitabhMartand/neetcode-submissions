class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                p = prices[j]-prices[i]
                maxp = max(p,maxp)
        return maxp