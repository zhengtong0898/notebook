#include <iostream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <numeric>


// 题目链接
// https://leetcode-cn.com/problems/queue-reconstruction-by-height/
class QueueReconstructionByHeight {
public:

    std::vector<std::vector<int>> 
    queue_reconstruction_by_height(std::vector<std::vector<int>>& people) {
        std::vector<std::vector<int>> result;
        int index = 0;
        std::sort(people.begin(), people.end());
        while (people.size() > 0) {
            int effect_index = index % people.size();
            std::vector<int> current_people = people[effect_index];

            int ge_count = 0;
            for (auto item : result)
                if (item[0] >= current_people[0])
                    ge_count += 1;

            if (ge_count >= current_people[1]) {
                result.push_back(people[effect_index]);
                people.erase(people.begin() + effect_index);
                index = -1;
            }
            index += 1;
        }
        return result;
    }
};


void test_1() {
    std::vector<std::vector<int>> people = { {7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2} };
    QueueReconstructionByHeight qrbh;
    std::vector<std::vector<int>> ss = qrbh.queue_reconstruction_by_height(people);
    std::vector<std::vector<int>> expect = { {5, 0}, {7, 0}, {5, 2}, {6, 1}, {4, 4}, {7, 1} };
    assert(ss == expect);
}


void test_2() {
    std::vector<std::vector<int>> people = { {6, 0}, {5, 0}, {4, 0}, {3, 2}, {2, 2}, {1, 4} };
    QueueReconstructionByHeight qrbh;
    std::vector<std::vector<int>> ss = qrbh.queue_reconstruction_by_height(people);
    std::vector<std::vector<int>> expect = { {4, 0}, {5, 0}, {2, 2}, {3, 2}, {1, 4}, {6, 0} };
    assert(ss == expect);
}


int main(void) {

    test_1();
    test_2();

    return 0;
}

