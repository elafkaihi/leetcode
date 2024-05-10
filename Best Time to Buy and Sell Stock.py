class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # the idea is to find the max and the min in the list 
        if len(prices) < 2:
            return 0
        i = 0
        max_profit = 0
        for j in range(1,len(prices)):
            actual_profit = prices[j]-prices[i]
            if actual_profit > max_profit:
                max_profit = actual_profit
            elif actual_profit < 0 :
                i = j
        
        return max_profit
