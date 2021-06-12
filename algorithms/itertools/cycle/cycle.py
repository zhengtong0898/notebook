from typing import List


# Infinite iterators: 无限迭代
def cycle_str(iterable: str):
    # 当 iterable 是字符串时, for循环会将字符串挨个挨个迭代出来.
    # 将其加入到 saved 列表中, 这是一个泛化过程.
    # 当 iterable 确定是列表或元祖时, 这段代码可以忽略掉.
    tolist = []
    for i in iterable:
        # 这里可以完全可以移除 yield,
        # 但是当 iterable 无限巨大时,
        # 会导致 tolist 过程会非常漫长.
        yield i
        tolist.append(i)

    while tolist:
        for i in tolist:
            yield i


def simple_test():
    text = "ABCD"
    for i in cycle_str(text):
        print(i)


def main():
    simple_test()


if __name__ == '__main__':
    main()
