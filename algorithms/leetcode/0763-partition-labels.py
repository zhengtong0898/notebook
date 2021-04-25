

# 题目链接
# https://leetcode-cn.com/problems/partition-labels/
class PartitionLabels:

    def partition_labels(self, s: str):
        # 字典具有唯一性, 这里将为每个字符仅保留其出现在字符串中最后一次的位置.
        lastcharmap = {char: index for index, char in enumerate(s)}

        result = []
        begin, end = 0, 0
        for index, char in enumerate(s):

            # 获取一个字母的最后个位置; 两种情况:
            # 1. 若当前字母的最后一次位置, 比当前 end 大, 那么后续操作就以当前字母为主去比较.
            # 2. 若当前字母的最后一次位置, 没有 end 大, 那么后续操作仍将以end的哪个字母为主去比较.
            end = max(end, lastcharmap[char])

            # 若当前索引是该字符的最后一个位置, 则切割.
            if index == end:
                result += [end - begin + 1]
                begin = index + 1

        return result


def test_1():
    s = "ababcbacadefegdehijhklij"

    pl = PartitionLabels()
    ss = pl.partition_labels(s)
    assert ss == [9, 7, 8]


def main():
    test_1()


if __name__ == '__main__':
    main()
