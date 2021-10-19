from typing import List


def decrement_v1(s: List[int]):
    rightmost_index = len(s) - 1
    for i in s:
        print(s[rightmost_index])
        rightmost_index -= 1


def decrement_v2(s: List[int]):
    rightmost_index = len(s)
    for i in range(len(s)):
        print(s[rightmost_index - i - 1])


if __name__ == '__main__':
    decrement_v1([1, 2, 3, 4])
    decrement_v2([1, 2, 3, 4])
