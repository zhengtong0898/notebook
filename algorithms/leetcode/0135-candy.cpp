#include <iostream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <numeric>


// 题目链接
// https://leetcode-cn.com/problems/candy/
class Candy {
public:

    int
    candy(std::vector<int>& ratings) {
        int ratings_size = ratings.size();
        std::vector<int> result(ratings_size, 1);       // 创建一个默认值为1的vector.

        for (int next_index = 1; next_index < ratings_size; next_index++) {
            int current_index = next_index - 1;
            if (ratings[next_index] > ratings[current_index])
                result[next_index] = result[current_index] + 1;
        }

        for (int current_index = ratings_size - 1; current_index > 0; current_index--) {
            int previous_index = current_index - 1;
            if (ratings[previous_index] > ratings[current_index])
                result[previous_index] = std::max(result[previous_index], result[current_index] + 1);
        }

        return std::accumulate(result.begin(), result.end(), 0);
    }

};


void test_1() {

    std::vector<int> ratings = { 1, 0, 2 };

    Candy candy;
    int ss = candy.candy(ratings);

    assert(ss == 5);

}


void test_2() {

    std::vector<int> ratings = { 1, 2, 2 };

    Candy candy;
    int ss = candy.candy(ratings);

    assert(ss == 4);

}


void test_3() {

    std::vector<int> ratings = { 1, 0, 4, 3, 2, 1, 0 };

    Candy candy;
    int ss = candy.candy(ratings);

    assert(ss == 18);

}


void test_4() {

    std::vector<int> ratings = { 1, 0, 4, 5, 6, 8, 7 };

    Candy candy;
    int ss = candy.candy(ratings);

    assert(ss == 18);

}


int main(void) {

    test_1();
    test_2();
    test_3();
    test_4();

    return 0;
}
