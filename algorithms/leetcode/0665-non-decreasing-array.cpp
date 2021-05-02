#include <iostream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <numeric>


// 题目链接
// https://leetcode-cn.com/problems/non-decreasing-array/
class NonDecreasingArray {
public:

    bool
    non_decreasing_array(std::vector<int>& nums) {
        int count = 0;

        for (int ni = 1; ni < nums.size(); ni++) {
            int ci = ni - 1;
            int cn = nums[ci], nn = nums[ni];

            if (cn > nn) {
                count++;

                if (count > 1)
                    return false;

                if (ci > 0) {
                    int pn = nums[ci - 1];
                    if (nn < pn)
                        nums[ni] = cn;
                }

            }
        }

        return true;
    }
};


void test_1() {
    std::vector<int> nums = { 4, 2, 3 };
    NonDecreasingArray nda;
    bool ss = nda.non_decreasing_array(nums);
    assert(ss == true);
}


void test_2() {
    std::vector<int> nums = { 4, 2, 1 };
    NonDecreasingArray nda;
    bool ss = nda.non_decreasing_array(nums);
    assert(ss == false);
}


int main(void) {

    test_1();
    test_2();

    return 0;
}

