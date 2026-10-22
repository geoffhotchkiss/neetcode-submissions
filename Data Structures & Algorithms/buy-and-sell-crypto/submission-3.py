class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Returns the maximum we can make. If no profit can be made, return 0. 
        keep track of profit, lowest valued stock, highest valued stock
        """

        lowest_seen = prices[0]
        highest_profit = 0

        for price in prices:
            profit = price - lowest_seen

            """
            highest_profit = max(highest_profit, profit)
            lowest_seen = min(lowest_seen, price)
            """
            if profit > highest_profit:
                highest_profit = profit

            if price < lowest_seen:
                lowest_seen = price
            

        return highest_profit