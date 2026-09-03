class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy one day and sell in the future
        # yesterday price
        max_profit = 0
        cheapest_price = prices[0]
        for i in range(len(prices)):
            today_price = prices[i]
            if i > 0 and min(cheapest_price, today_price) == cheapest_price:
                continue
            cheapest_price = today_price

            for j in range(i+1, len(prices)):
                max_profit = max(max_profit, prices[j] - today_price)
        
        return max_profit


        