#include <iostream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <numeric>


// 题目链接
// https://leetcode-cn.com/problems/can-place-flowers/
class CanPlaceFlower {
public:

    bool
    can_place_flower(std::vector<int>& flowerbed, int n) {

        int counter = 0;
        int pi = 0, ci = 0, ni = 0;

        for (ni = 1; ni < flowerbed.size(); ni++) {
            ci = ni - 1;
            if (flowerbed[pi] == 0 && flowerbed[ci] == 0 && flowerbed[ni] == 0)
                counter += 1;
            pi = ci;
        }

        return counter == n;

    }

};


void test_1() {

    std::vector<int> flowerbed = { 1, 0, 0, 0, 1 };
    CanPlaceFlower cpf;
    bool ss = cpf.can_place_flower(flowerbed, 1);
    assert(ss == true);

}


void test_2() {

    std::vector<int> flowerbed = { 1, 0, 0, 0, 1 };
    CanPlaceFlower cpf;
    bool ss = cpf.can_place_flower(flowerbed, 2);
    assert(ss == false);

}


void test_3() {

    std::vector<int> flowerbed = { 1, 0, 1, 0, 1 };
    CanPlaceFlower cpf;
    bool ss = cpf.can_place_flower(flowerbed, 0);
    assert(ss == true);

}


void test_4() {

    std::vector<int> flowerbed = { 1, 0, 1, 0, 1 };
    CanPlaceFlower cpf;
    bool ss = cpf.can_place_flower(flowerbed, 2);
    assert(ss == false);

}


int main(void) {

    test_1();
    test_2();
    test_3();
    test_4();

    return 0;
}
