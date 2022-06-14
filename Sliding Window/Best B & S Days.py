class Solution:
    def maxProfit(self, prices):
        buy, sell = 0, 1
        max_profit = 0
        while sell <= len(prices) - 1:
            profit = prices[sell] - prices[buy]
            if prices[buy] > prices[sell]:
                buy += 1
                sell = buy + 1
            elif prices[buy] < prices[sell] and profit > max_profit:
                max_profit = profit
                sell += 1
            else:
                sell += 1
        return max_profit


if __name__ == '__main__':
    s = Solution()

    # prices = [7,1,5,3,6,4]

    prices = [2,1,4]
    print(s.maxProfit(prices))