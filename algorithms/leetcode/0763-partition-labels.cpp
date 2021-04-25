#include <iostream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <numeric>


// 题目链接
// https://leetcode-cn.com/problems/partition-labels/
class PartitionLabels {
public:

    std::vector<int>
    partition_labels(std::string s) {

        // 创建一个vector, 26个元素, 全部初始为0.
        std::vector<int> pos(26, 0);


        // 这个代码块最终要打到的目的是:
        // 为每个字符仅保留其出现在字符串中最后一次的索引位置.
        for (int i = 0; i < s.size(); i++) {
            int index = s[i] - 'a';             // 计算hash值
            pos[index] = i;                     // 写入该字符的当前的索引位置.
        }

        std::vector<int> result;
        int begin = 0, end = 0;
        for (int i = 0; i < s.size(); i++) {
            int index = s[i] - 'a';
            end = std::max(end, pos[index]);

            if (i == end) {
                result.push_back(end - begin + 1);
                begin = i + 1;
            }
        }

        return result;
    }
};


void test_1() {
    std::string ss = "ababcbacadefegdehijhklij";
    PartitionLabels pl;
    std::vector<int> vss = pl.partition_labels(ss);
    std::vector<int> expected { 9, 7, 8 };
    assert(vss == expected);
}



int main(void) {

    test_1();

    return 0;
}
