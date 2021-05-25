

class GroupBy:

    def __init__(self, iterable):
        self.it = iter(iterable)
        self.key = self.value = self.groupkey = object()

    def __iter__(self):
        return self

    def __next__(self):
        """
        当前方法负责处理 for 循环, 即: 每迭代一次, 都会执行一次当前方法.
        当前方法负责处理 next() 指令, 即: 每执行一次next()指令, 都会执行一次当前方法.
        """
        while self.key == self.groupkey:
            self.value = next(self.it)
            self.key = self.value

        self.groupkey = self.key
        return self.groupkey, self.grouper()

    def grouper(self):
        """
        作为一个类成员方法, 就应该知道当前类有哪些内部属性, 能直接使用就直接使用,
        除非当前类没有提供必要的属性, 才会考虑使用参数来驱动方法.
        """
        while self.key == self.groupkey:
            yield self.value
            try:
                self.value = next(self.it)
            except StopIteration:
                return
            self.key = self.value


def simple_test():
    text = 'AAAABBBCCDAABBB'
    group_by = GroupBy(text)
    print(next(group_by))
    print(next(group_by))
    # ss = [(k, list(g)) for k, g in GroupBy(text)]
    # assert ss == [('A', ['A', 'A', 'A', 'A']),
    #               ('B', ['B', 'B', 'B']),
    #               ('C', ['C', 'C']),
    #               ('D', ['D']),
    #               ('A', ['A', 'A']),
    #               ('B', ['B', 'B', 'B'])]

    # text = ''
    # ss = [(k, list(g)) for k, g in GroupBy(text)]
    # print(ss)


def main():
    simple_test()


if __name__ == '__main__':
    main()
