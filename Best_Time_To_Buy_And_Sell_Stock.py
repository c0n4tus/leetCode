class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        df=[0] * len(prices)
        min_price=prices[0]
        
        for i in range(len(prices)):
            df[i] = max(df[i-1], prices[i] - min_price)
            min_price=min(prices[i],min_price)
        
        return df[-1]