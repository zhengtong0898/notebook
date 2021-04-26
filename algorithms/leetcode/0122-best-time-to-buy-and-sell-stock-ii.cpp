#include <iostream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <numeric>


// 题目链接
// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
class BestTimeToBuyAndSellStockII {
public:

    int
    best_time_to_buy_and_sell_stock_ii(std::vector<int> & prices) {
        std::vector<int> s;
        for (int ni = 1; ni < prices.size(); ni++) {
            int ci = ni - 1;
            int max_one = std::max(prices[ni] - prices[ci], 0);
            s.push_back(max_one);
        }

        return std::accumulate(s.begin(), s.end(), 0);
    }

};


void test_1() {
    std::vector<int> prices = { 7, 1, 5, 3, 6, 4 };
    BestTimeToBuyAndSellStockII bttbassii;
    int ss = bttbassii.best_time_to_buy_and_sell_stock_ii(prices);
    assert(ss == 7);
}


void test_2() {
    std::vector<int> prices = { 1, 2, 3, 4, 5 };
    BestTimeToBuyAndSellStockII bttbassii;
    int ss = bttbassii.best_time_to_buy_and_sell_stock_ii(prices);
    assert(ss == 4);
}


void test_3() {
    std::vector<int> prices = { 7, 6, 4, 3, 1 };
    BestTimeToBuyAndSellStockII bttbassii;
    int ss = bttbassii.best_time_to_buy_and_sell_stock_ii(prices);
    assert(ss == 0);
}


int main(void) {

    test_1();
    test_2();
    test_3();

    return 0;
}

