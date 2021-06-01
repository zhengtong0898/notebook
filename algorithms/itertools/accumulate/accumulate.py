import operator


def accumulate(iterable, func=operator.add, initial=None):
    """ 累加算法 """
    it = iter(iterable)

    # 这段代码是为了处理 initial 是 None 和 非None 两种情况.
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return

    yield total

    for i in it:
        total = func(total, i)
        yield total


def main():
    s = list(accumulate([1,2,3,4]))
    assert s == [1, 3, 6, 10]
    s = list(accumulate([1, 2, 3, 4], func=operator.mul))
    assert s == [1, 2, 6, 24]


if __name__ == '__main__':
    main()
