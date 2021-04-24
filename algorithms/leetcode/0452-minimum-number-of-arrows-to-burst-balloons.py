from typing import List


# 题目链接
# https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/
class MinimumNumberOfArrowsToBurstBalloons:

    def minimum_number_of_arrows_to_burst_balloons(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count, previous_second = 0, 0
        for first, second in points:
            if first > previous_second:
                count += 1
                previous_second = second
        return count

    def minimum_number_of_arrows_to_burst_balloons_me(self, points: List[List[int]]) -> int:
        points.sort()
        points_size: int = len(points)

        count = 0
        anyhit = False
        temp = []

        for next_index in range(1, points_size):
            current_index = next_index - 1
            current_point = points[current_index]
            next_point = points[next_index]

            if next_point[0] <= current_point[1] <= next_point[1]:

                anyhit = True
                if not temp:
                    temp = [max(current_point[0], next_point[0]),
                            min(current_point[1], next_point[1])]
                    count += 1
                    continue

                elif temp[0] <= current_point[1] <= temp[1]:
                    temp = [max(current_point[0], next_point[0], temp[0]),
                            min(current_point[1], next_point[1], temp[1])]
                    count += 1

                else:
                    temp = []

            else:
                count += 1
                temp = []

        if not anyhit:
            count += 1

        return count


def test_1():

    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    mnoabb = MinimumNumberOfArrowsToBurstBalloons()
    ss1 = mnoabb.minimum_number_of_arrows_to_burst_balloons(points)
    ss2 = mnoabb.minimum_number_of_arrows_to_burst_balloons_me(points)
    assert ss1 == 2
    assert ss2 == 2


def test_2():

    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    mnoabb = MinimumNumberOfArrowsToBurstBalloons()
    ss1 = mnoabb.minimum_number_of_arrows_to_burst_balloons(points)
    ss2 = mnoabb.minimum_number_of_arrows_to_burst_balloons_me(points)
    assert ss1 == 4
    assert ss2 == 4


def test_3():

    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    mnoabb = MinimumNumberOfArrowsToBurstBalloons()
    ss1 = mnoabb.minimum_number_of_arrows_to_burst_balloons(points)
    ss2 = mnoabb.minimum_number_of_arrows_to_burst_balloons_me(points)
    assert ss1 == 2
    assert ss2 == 2


def test_4():

    points = [[1, 2]]
    mnoabb = MinimumNumberOfArrowsToBurstBalloons()
    ss1 = mnoabb.minimum_number_of_arrows_to_burst_balloons(points)
    ss2 = mnoabb.minimum_number_of_arrows_to_burst_balloons_me(points)
    assert ss1 == 1
    assert ss2 == 1


def test_5():

    points = [[2,3],[2,3]]
    mnoabb = MinimumNumberOfArrowsToBurstBalloons()
    ss1 = mnoabb.minimum_number_of_arrows_to_burst_balloons(points)
    ss2 = mnoabb.minimum_number_of_arrows_to_burst_balloons_me(points)
    assert ss1 == 1
    assert ss2 == 1


def main():

    test_1()
    test_2()
    test_3()
    test_4()
    test_5()


if __name__ == '__main__':
    main()