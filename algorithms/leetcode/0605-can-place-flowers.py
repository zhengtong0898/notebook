from typing import List


# 题目链接
# https://leetcode-cn.com/problems/can-place-flowers/
class CanPlaceFlower:

    def can_place_flower(self, flowerbed: List[int], n: int) -> bool:

        counter = 0
        pi, ci, ni = 0, 0, 0

        for ni in range(1, len(flowerbed)):
            ci = ni - 1
            if not any([flowerbed[pi], flowerbed[ci], flowerbed[ni]]):
                counter += 1
            pi = ci

        return counter == n


def test_1():
    flowerbed = [1, 0, 0, 0, 1]
    cpf = CanPlaceFlower()
    ss = cpf.can_place_flower(flowerbed, n=1)
    assert ss is True


def test_2():
    flowerbed = [1, 0, 0, 0, 1]
    cpf = CanPlaceFlower()
    ss = cpf.can_place_flower(flowerbed, n=2)
    assert ss is False


def test_3():
    flowerbed = [1, 0, 1, 0, 1]
    cpf = CanPlaceFlower()
    ss = cpf.can_place_flower(flowerbed, n=0)
    assert ss is True


def test_4():
    flowerbed = [1, 0, 1, 0, 1]
    cpf = CanPlaceFlower()
    ss = cpf.can_place_flower(flowerbed, n=2)
    assert ss is False


def main():

    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
