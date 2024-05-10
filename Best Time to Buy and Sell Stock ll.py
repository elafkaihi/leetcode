class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            actual_profit = prices[j] - prices[i]
            if actual_profit > 0 :
                max_profit += actual_profit
            i += 1
            j += 1 
        return max_profit
