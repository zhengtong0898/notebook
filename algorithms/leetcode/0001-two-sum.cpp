#include <iostream>
#include <vector>
#include <unordered_map>
#include <assert.h>


class TwoSum {
public:

    // 时间复杂度: O(n^2)
    std::vector<int>
    two_sum_1(std::vector<int>& nums, int target) {
        std::vector<int> indexes;
        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if ((nums[i] + nums[j]) == target) {
                    indexes.push_back(i);
                    indexes.push_back(j);
                    return indexes;
                }
            }
        }
        return indexes;
    }

    // 时间复杂度: O(n)
    std::vector<int>
    two_sum_2(std::vector<int>& nums, int target) {
        std::vector<int> indexes;
        std::unordered_map<int, int> dict;
        for (int i = 0; i < nums.size(); i++) {
            int ss = target - nums[i];
            if (dict.find(ss) != dict.end()) {              // 查找: O(1)
                indexes.push_back(dict[ss]);
                indexes.push_back(i);
                return indexes;
            }
            dict.insert(std::make_pair(nums[i], i));        // 插入: O(1)
        }
        return indexes;
    }
};


int main(void) {

    // 准备数据
    std::vector<int> data = { 2, 7, 11, 15 };
    int target = 9;

    // 断言数据
    std::vector<int> expected = { 0, 1 };


    // 测试-1
    TwoSum ts_1 = TwoSum();
    std::vector<int> indexes_1 = ts_1.two_sum_1(data, target);
    assert(indexes_1 == expected);

    // 测试-1
    TwoSum ts_2 = TwoSum();
    std::vector<int> indexes_2 = ts_2.two_sum_2(data, target);
    assert(indexes_2 == expected);

    return 0;
}
