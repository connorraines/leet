class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < 0:
                raise ValueError("Prices cannot be negative")
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit