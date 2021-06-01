from typing import List


def accumulate_add(iterable: List[int]):
    """ 累加算法 """
    total = 0
    for i in iterable:
        total += i
        yield total


def main():
    s = list(accumulate_add([1, 2]))
    assert s == [1, 3]
    s = list(accumulate_add([1, 2, 3]))
    assert s == [1, 3, 6]
    s = list(accumulate_add([1, 2, 3, 4]))
    assert s == [1, 3, 6, 10]


if __name__ == '__main__':
    main()
