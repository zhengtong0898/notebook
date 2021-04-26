from typing import List


# 题目链接
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
class BestTimeToBuyAndSellStockII:

    def best_time_to_buy_and_sell_stock_ii(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

    def best_time_to_buy_and_sell_stock_ii_debug(self, prices):
        s = []
        for i in range(len(prices) - 1):
            next_item = prices[i + 1]
            current_item = prices[i]
            calcu = next_item - current_item
            s.append(max(calcu, 0))
        return sum(s)


    def best_time_to_buy_and_sell_stock_ii_me(self, prices: List[int]) -> int:
        prices_size = len(prices)
        last_index = prices_size - 1

        profit = 0
        hold_ticket = False

        for ni in range(1, prices_size):
            ci = ni - 1

            # 买入
            if prices[ci] < prices[ni]:
                if not hold_ticket:
                    hold_ticket = True
                    profit -= prices[ci]

            # 卖掉
            if prices[ci] > prices[ni]:
                if hold_ticket:
                    hold_ticket = False
                    profit += prices[ci]

            # 卖掉
            if hold_ticket and ni == last_index:
                hold_ticket = False
                profit += max(prices[ci], prices[ni])

        return profit


def test_1():

    prices = [7, 1, 5, 3, 6, 4]
    bttbassii = BestTimeToBuyAndSellStockII()
    ss1 = bttbassii.best_time_to_buy_and_sell_stock_ii(prices)
    ss2 = bttbassii.best_time_to_buy_and_sell_stock_ii_me(prices)
    assert ss1 == 7
    assert ss2 == 7


def test_2():

    prices = [1, 2, 3, 4, 5]
    bttbassii = BestTimeToBuyAndSellStockII()
    ss1 = bttbassii.best_time_to_buy_and_sell_stock_ii(prices)
    ss2 = bttbassii.best_time_to_buy_and_sell_stock_ii_me(prices)
    assert ss1 == 4
    assert ss2 == 4


def test_3():

    prices = [7, 6, 4, 3, 1]
    bttbassii = BestTimeToBuyAndSellStockII()
    ss1 = bttbassii.best_time_to_buy_and_sell_stock_ii(prices)
    ss2 = bttbassii.best_time_to_buy_and_sell_stock_ii_me(prices)
    assert ss1 == 0
    assert ss2 == 0


def main():

    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    main()

