

count = 0


def binary_search_simple(items: list, item, reset_count=True) -> bool:
    # 统计相关
    global count
    if reset_count: count = 0
    count += 1

    if not items: return False
    midpoint = len(items) // 2                                                          # 对半整除
    midvalue = items[midpoint]
    if item == midvalue: return True
    if item > midvalue:
        # 这里 + 1 是因为已经做过 item 不等于 midvalue 的比较,
        # 所以这里就不需要再把 midvalue 当作比较区间成员.
        # 例如:
        # items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # midpoint = len(s) // 2 == 5
        # items[midpoint] == items[5] == 6              其中 6 != 5
        # items[0:5] == [1,2,3,4,5]
        # items[5+1:] == [7,8,9,10]                     那么这里6已经比较过了, 就不需要再比较, 把他剔除.
        return binary_search_simple(items[midpoint + 1:], item, reset_count=False)
    else:
        return binary_search_simple(items[:midpoint], item, reset_count=False)


if __name__ == '__main__':
    assert binary_search_simple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == True
    assert count == 3
    assert binary_search_simple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == True
    assert count == 4

    # 一亿次, 26次匹配
    ss = list(range(100000000))
    assert binary_search_simple(ss, 1) == True
    assert count == 26
