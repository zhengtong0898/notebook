from typing import List


# 题目链接
# https://leetcode-cn.com/problems/queue-reconstruction-by-height/
class QueueReconstructionByHeight:

    def queue_reconstruction_by_height(self, people: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []

        index = 0
        people.sort()
        while people:
            effect_index = index % len(people)
            current_people = people[effect_index]
            ge_count = len([item for item in result if item[0] >= current_people[0]])
            if ge_count == current_people[1]:
                result.append(people.pop(effect_index))
                index = -1
            index += 1

        return result


def test_1():
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    qrbh = QueueReconstructionByHeight()
    ss = qrbh.queue_reconstruction_by_height(people)
    assert ss == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]


def test_2():
    people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    qrbh = QueueReconstructionByHeight()
    ss = qrbh.queue_reconstruction_by_height(people)
    assert ss == [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]


def main():

    test_1()
    test_2()


if __name__ == '__main__':
    main()

