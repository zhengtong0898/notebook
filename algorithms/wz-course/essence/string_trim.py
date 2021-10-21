from typing import List


def trim(s: List[str]):
    n = len(s)
    index = 0                          # 标记已经替换的字符位置
    cursor = 0                         # 游标用于标记循环所处的位置, 同时它还保证时间复杂度是 O(n).
                                       # 游标用于

    # 数组的左侧和右侧的处理原则是: 丢弃空字符.
    for i in s:
        if i != " ": break
        cursor += 1

    # 数组的中间段的处理原则是: 多个连续存在的空格仅保留一个空格.
    while cursor < n:

        if s[cursor] == " ":
            # 边界保护
            next_cursor = cursor + 1
            if (next_cursor + 1) >= n:
                cursor += 1
                continue

            # 当下一个游标索引位置是空时, 表示存在连续的空格, 此时游标向右移动一个位置.
            if s[next_cursor] == " ":
                cursor += 1
                continue

            # 当程序来到这里时, 意味着一个或多个空格处理完毕, 不论是1个空格或多个空格, 都仅保留一个空格.
            s[index] = s[cursor]
        else:
            # 当 index == cursor 时, 交换操作等于什么都没有做.
            # 当 index != cursor 时, 交换操作等于将空格往右边挪, 将字符往左边挪.
            s[index] = s[cursor]

        # 游标无论如何都会递增1.
        cursor += 1
        # 代码来到这里, 意味着执行完交换操作, 这里递增1是为了下一个循环做准备.
        index += 1


if __name__ == '__main__':
    inputs = [i for i in "   hello   a       world!   "]
    expect = [i for i in "hello a world!"]
    trim(s=inputs)
    assert inputs[0: len(expect)] == expect
