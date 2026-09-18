class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0

        min_element = prices[0]
        for i in range(len(prices)):
            
            if min_element > prices[i]:
                min_element = prices[i]

            else:
                result = 0
                result = prices[i] - min_element
                if result > max_profit:
                    max_profit = result
        return max_profit
        

        