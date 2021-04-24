#include <iostream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <numeric>


// 题目链接
// https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/
class MinimumNumberOfArrowsToBurstBalloons {
public:

    int
    minimum_number_of_arrows_to_burst_balloons(std::vector<std::vector<int>>& points) {

        std::sort(points.begin(),
                  points.end(),
                  [](std::vector<int>& a, std::vector<int>& b) {
                  return a[1] < b[1];
        });

        int count = 0, previous_second = 0;
        for (auto& point : points) {
            if (point[0] > previous_second) {
                count += 1;
                previous_second = point[1];
            }
        }

        return count;
    }

};


void test_1() {

    std::vector<std::vector<int>> points = { {10, 16}, {2, 8}, {1, 6}, {7, 12} };
    MinimumNumberOfArrowsToBurstBalloons mnoabb;
    int ss = mnoabb.minimum_number_of_arrows_to_burst_balloons(points);
    assert(ss == 2);

}


void test_2() {

    std::vector<std::vector<int>> points = { {1, 2}, {3, 4}, {5, 6}, {7, 8} };
    MinimumNumberOfArrowsToBurstBalloons mnoabb;
    int ss = mnoabb.minimum_number_of_arrows_to_burst_balloons(points);
    assert(ss == 4);

}


void test_3() {

    std::vector<std::vector<int>> points = { {1, 2}, {2, 3}, {3, 4}, {4, 5} };
    MinimumNumberOfArrowsToBurstBalloons mnoabb;
    int ss = mnoabb.minimum_number_of_arrows_to_burst_balloons(points);
    assert(ss == 2);

}


void test_4() {

    std::vector<std::vector<int>> points = { {1, 2} };
    MinimumNumberOfArrowsToBurstBalloons mnoabb;
    int ss = mnoabb.minimum_number_of_arrows_to_burst_balloons(points);
    assert(ss == 1);

}


void test_5() {

    std::vector<std::vector<int>> points = { {2, 3}, {2, 3} };
    MinimumNumberOfArrowsToBurstBalloons mnoabb;
    int ss = mnoabb.minimum_number_of_arrows_to_burst_balloons(points);
    assert(ss == 1);

}


int main(void) {

    test_1();
    test_2();
    test_3();
    test_4();
    test_5();

    return 0;
}
