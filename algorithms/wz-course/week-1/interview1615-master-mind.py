import collections
from typing import List


class Solution:

    """
    珠玑妙算游戏（the game of master mind）的玩法如下。

    计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。
    例如，计算机可能有RGGB 4种（槽1为红色，槽2、3为绿色，槽4为蓝色）。作为用户，你试图猜出颜色组合。
    打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；
    要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。

    给定一种颜色组合solution和一个猜测guess，
    编写一个方法返回猜中和伪猜中的次数answer，
    其中answer[0]为猜中的次数，answer[1]为伪猜中的次数。

    https://leetcode-cn.com/problems/master-mind-lcci/

    已知条件:
    1. len(solution) = len(guess) = 4
    2. solution 和 guess 仅包含"R","G","B","Y"这4种字符
    """

    def masterMind(self, solution: str, guess: str) -> List[int]:
        """
        1. 相同位置相同字符, 记录下来是"猜中".
        2. 不同位置相同字符, 记录下来是"伪猜中".
        """
        same_position_same_char = 0
        diff_position_same_char = 0

        all_map = {"R": [0, 0], "G": [0, 0], "B": [0, 0], "Y": [0, 0]}
        for i in solution:
            all_map[i][0] += 1

        for index, char in enumerate(guess):
            if solution[index] == guess[index]:
                same_position_same_char += 1
                all_map[guess[index]][0] -= 1
            else:
                all_map[guess[index]][1] += 1

        for k, v in all_map.items():
            if all(v):
                diff_position_same_char += (min(v)*2) // 2

        return [same_position_same_char, diff_position_same_char]

    def masterMind_2(self, solution: str, guess: str) -> List[int]:
        # 相同位置相同字符, 记录下来是"猜中".
        a = sum(i == j for i, j in zip(solution, guess))
        # 建立 solution 字典(类型是 Counter)
        solution_dict = collections.Counter(solution)
        # 建立 guess 字典(类型是 Counter)
        guess_dict = collections.Counter(guess)
        # AND 操作:
        # 1. 仅保留两边都相同的k/v.
        # 2. 两个相同k, 保留小的那个值.
        # 高价值参考资料:  https://realpython.com/python-bitwise-operators/#reader-comments
        all_dict = solution_dict & guess_dict
        # 仅取数值(类型是List[int])
        b = all_dict.values()
        b = sum(b)
        # [相同位置相同字符的个数, 不同位置相同字符的个数]
        return [a, b - a]


def test():
    solution = Solution()

    solu = "RGBY"
    guess = "GGRR"
    expect = [1, 1]
    result = solution.masterMind(solution=solu, guess=guess)
    result = solution.masterMind_2(solution=solu, guess=guess)
    assert result == expect

    solu = "RGRB"
    guess = "BBBY"
    expect = [0, 1]
    result = solution.masterMind(solution=solu, guess=guess)
    result = solution.masterMind_2(solution=solu, guess=guess)
    assert result == expect

    solu = "YBBY"
    guess = "GYYB"
    expect = [0, 3]
    result = solution.masterMind(solution=solu, guess=guess)
    result = solution.masterMind_2(solution=solu, guess=guess)
    assert result == expect

    solu = "GGBB"
    guess = "RBYB"
    expect = [1, 1]
    result = solution.masterMind(solution=solu, guess=guess)
    result = solution.masterMind_2(solution=solu, guess=guess)
    assert result == expect


def main():
    test()


if __name__ == '__main__':
    main()
