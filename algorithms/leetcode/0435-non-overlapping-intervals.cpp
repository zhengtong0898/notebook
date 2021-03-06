#include<assert.h>
#include<vector>
#include<algorithm>


// 题目链接
// https://leetcode-cn.com/problems/non-overlapping-intervals/
class AssignCookies {
public:

    int
    assign_cookie(std::vector<int>& greed, std::vector<int>& size) {

        std::sort(greed.begin(), greed.end());
        std::sort(size.begin(), size.end());

        int child_flag = 0;
        int cookie_flag = 0;

        while (cookie_flag < size.size() && child_flag < greed.size()) {
            bool can_feed = size[cookie_flag] >= greed[child_flag];
            if (can_feed) child_flag += 1;
            cookie_flag += 1;
        }

        return child_flag;

    }

};


void assign_cookie_test_1() {

    std::vector<int> greed = { 1, 2, 3 };
    std::vector<int> size = { 1, 1 };

    AssignCookies ac;
    int ss = ac.assign_cookie(greed, size);

    assert(ss == 1);

}


void assign_cookie_test_2() {

    std::vector<int> greed = { 1, 2 };
    std::vector<int> size = { 1, 2, 3 };

    AssignCookies ac;
    int ss = ac.assign_cookie(greed, size);

    assert(ss == 2);

}


void assign_cookie_test_3() {

    std::vector<int> greed = { 1, 2, 3, 4, 5 };
    std::vector<int> size = { 2, 9 };

    AssignCookies ac;
    int ss = ac.assign_cookie(greed, size);

    assert(ss == 2);

}


int assign_cookie_main(void) {

    assign_cookie_test_1();
    assign_cookie_test_2();
    assign_cookie_test_3();

    return 0;
}
