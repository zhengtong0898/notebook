

"""
按指定数量列出不重复(非穷尽)的组合, 例如:
combinations('ABCD', 2) -> 'AB',   'AC',  'AD',  'BC', 'BD', 'CD'
combinations('ABCD', 3) -> 'ABC', 'ABD', 'ACD', 'BCD'

重复指的是:
'ABC' -> 'CBA'
'ABD' -> 'DBA'
'ACD' -> 'DCA'
'BCD' -> 'DCB'
"""


def combinations(iterable, comb_size):

    """
    comb_size: 组合对象的大小,
               当 comb_size = 2 时, 表示每个组合的长度是2.
               当 comb_size = 3 时, 表示每个组合的长度是3.
    """

    # 假设 iterable = 'ABCD' 时, 处理场景是 str, pool = ('A', 'B', 'C', 'D')
    # 假设 iterable = ['apple', 'orange', 'banana'] 时, 处理场景是 list, pool = ('apple', 'orange', 'banana')
    # 假设 iterable = {'a': 1, 'b': 2, 'c': 3} 时, 处理场景是 dict, pool = ('a', 'b', 'c')
    # 所以这里的目的是找到一种通用的办法来泛化不同类型的操作.
    tuple_value = tuple(iterable)
    tuple_size = len(tuple_value)

    invalid_size = comb_size > tuple_size
    if invalid_size: return

    # indices 是一个索引位置的集合.
    # 当 comb_size = 2 时, indices = [index_1, index_2].
    # 当 comb_size = 3 时, indices = [index_1, index_2, index_3].
    # 需要注意的是: indices 不是 slice; indices是一个索引集合, slice是一个分片.
    indices = list(range(comb_size))
    indices_len = len(indices)
    yield tuple(tuple_value[i] for i in indices)

    while True:

        # 这个代码块检查 indices 的边界有效性.
        # 假设: iterable = 'ABCD', comb_size = 2;
        # indices 的有效范围是: indices[0, 1] -- indices[2, 3]
        #
        # indices[0, 0] 对应的是 (iterable[0], iterable[0]) 对应的是 ('A', 'A');    不报错, 无效的组合
        # indices[0, 1] 对应的是 (iterable[0], iterable[1]) 对应的是 ('A', 'B');    不报错, 有效的组合
        # indices[2, 3] 对应的是 (iterable[2], iterable[3]) 对应的是 ('C', 'D');    不报错, 有效的组合
        # indices[3, 3] 对应的是 (iterable[3], iterable[3]) 对应的是 ('D', 'D');    不报错, 无效的组合
        #
        # reversed(range(indices_len)):  从 indices 最后一个元素开始比较.
        for i in reversed(range(indices_len)):

            # 它的运作机制是： i = 1; or i = 0;
            # i = 1 时, 1 + 4 - 2 = 3, 这里 3 表示最后一个元素, 不可以再做追加操作.
            # i = 0 时, 0 + 4 - 2 = 2, 这里 2 表示最后一个元素, 不可以再做追加操作.
            if indices[i] != i + tuple_size - comb_size:
                break
            else:
                # 当 i = 1, 且 indices[1] == 3 时, 会一直进入这里.
                # 当 i = 0, 且 indices[0] == 2 时, 也会进入到这里
                continue
        else:
            # 当 for 循环没有触发 break 时, 会进入这里, 跳出 while 循环, 也跳出函数.
            return

        # 当 i == 1, 且 indices[1] == 3 时, 是无法抵达这里的,
        # 因为会被上面的 continue 进入下一个 i(即: i == 0).
        # 代码能来到这里, 表示 indices[i] 不是最后一个元素.
        pass

        # iterable[i] 右移一个位置.
        # 当 i == 1, indices_len == 2, indices == [0, 1], iterable[0] == 'A', iterable[1] == 'B';
        # 右移一个位置:                  indices == [0, 2], iterable[0] == 'A', iterable[2] == 'C';
        # 再右移一个位置:                indices == [0, 3], iterable[0] == 'A', iterable[3] == 'D';
        #
        # 当 i == 0, indices_len == 2, indices == [0, 3], iterable[0] == 'A', iterable[3] == 'D';
        # 右移一个位置:                  indices == [1, 3], iterable[1] == 'B', iterable[3] == 'D';
        indices[i] += 1

        # 当 i == 0, comb_size == 2, j == 1, indices == [1, 3], iterable[1] == 'B', iterable[3] == 'D'时;
        # indices[j - 1] + 1 == indices[0] + 1 == 1 + 1 == 2;
        # indices[j] = indices[j - 1] + 1 == indices[1] = 2;
        # (重点)这个动作可以被称为是复位,
        # (重点)由于复位后的 indices[1] 不是最后一个元素,
        # (重点)所以 i 会再次 == 1, 直到 indices[1] 再次抵达最后一个元素, 那么就会再次执行复位动作, 循环往复.
        for j in range(i+1, comb_size):
            indices[j] = indices[j-1] + 1

        yield tuple(tuple_value[i] for i in indices)


def main():
    ss = list(combinations('ABCD', 2))
    assert ss == [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]


if __name__ == '__main__':
    main()
