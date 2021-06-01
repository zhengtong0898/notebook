from typing import List


# Infinite iterators: 无限迭代
def cycle_str(iterable: str):
    tolist = []

    # 当 iterable 是字符串时, for循环会将字符串挨个挨个迭代出来.
    # 将其加入到 saved 列表中, 这是一个泛化过程.
    #
    # 当 iterable 确定是列表或元祖时, 这段代码可以忽略掉.
    for i in iterable:
        yield i
        tolist.append(i)

    while tolist:
        for i in tolist:
            yield i


def cycle_list(iterable: List[str]):
    while True:
        for i in iterable:
            yield i


def simple_test_1():
    text = "ABCD"
    for i in cycle_str(text):
        print(i)


def simple_test_2():
    text = ["a", "b", "c", "d"]
    for i in cycle_list(text):
        print(i)


def simple_test_3():
    text_1 = "ABCD"
    text_2 = ["a", "b", "c", "d"]

    cs = cycle_str(text_1)
    cl = cycle_list(text_2)
    while True:
        print(" cycle_str: ", next(cs))
        print("cycle_list: ", next(cl))


def main():
    simple_test_1()
    simple_test_2()
    simple_test_3()


if __name__ == '__main__':
    main()
