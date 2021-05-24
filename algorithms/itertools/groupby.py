"""
# itertools.groupby 的原理、使用场景.


text = 'AAAABBBCCDAABBB'
s = [(k, list(g)) for k, g in groupby(text)]
print(s)
# [('A', ['A', 'A', 'A', 'A']),
#  ('B', ['B', 'B', 'B']),
#  ('C', ['C', 'C']),
#  ('D', ['D']),
#  ('A', ['A', 'A']),
#  ('B', ['B', 'B', 'B'])]


s = {k: list(g) for k, g in groupby(text)}
print(s)
# {'A': ['A', 'A'],
#  'B': ['B', 'B', 'B'],
#  'C': ['C', 'C'],
#  'D': ['D']}


text = 'AAAABBBCCD'
s = [(k, list(g)) for k, g in groupby(text)]
print(s)
# [('A', ['A', 'A', 'A', 'A']),
#  ('B', ['B', 'B', 'B']),
#  ('C', ['C', 'C']),
#  ('D', ['D'])]


s = {k: list(g) for k, g in groupby(text)}
print(s)
# {'A': ['A', 'A', 'A', 'A'], 
#  'B': ['B', 'B', 'B'], 
#  'C': ['C', 'C'], 
#  'D': ['D']}
"""


# https://docs.python.org/3/library/itertools.html#itertools.groupby
class GroupBy:

    def __init__(self, iterable, key=None):
        """
        :param iterable:
        :param key: 参数 key 的命名是为了与 sorted 的参数 key 命名保持一致.
        """

        # TODO: key使用案例, 待补充.
        self.keyfunc = lambda x: x if key is None else key

        # 将 iterable 转换成迭代器.
        self.it = iter(iterable)

        # 这里不能写成: self.key, self.value, self.groupkey = None
        # 的原因是, 当 iterable 是一组 [None, None, None] 时,
        # 会导致无法进入分组函数, 而是在生成groupkey的过程中报错.
        self.key = self.value = self.groupkey = object()

    def __iter__(self):
        return self

    def _grouper(self, groupkey):
        # 提取一组与 groupkey 相同的值.
        while self.key == groupkey:
            yield self.value

            # 由于 _grouper 函数是在 __next__ 函数内执行,
            # 因此当遇到 StopIteration 时, 也不会报错, 而是跳出 __next__ 函数.
            # 这里为了让逻辑代码能持续运行下去, 采取 try 来防止跳出 __next__ 函数.
            # 采取 return 仅跳出当前 _grouper 函数.
            # TODO: 待确认.
            try:
                self.value = next(self.it)
            except StopIteration:
                return
            self.key = self.keyfunc(self.value)

    def __next__(self):
        # 初始状态下, self.key == self.groupkey, 此时试图提取 next(self.it) 下一个值.
        # 在这里, next(self.it) 遇到 StopIteration 不会报错, 而是跳出 __next__ 函数.
        # 非初始状态下, self.key != self.groupkey, 因此不会进入while循环.
        #
        # 也就是说, 只有在初始状态下才会进入while循环,
        # TODO: 那是否可以将 while 替换成 if ?
        #       if self.key == self.groupkey:
        #           self.value = next(self.it)
        #           self.key = self.keyfunc(self.value)
        while self.key == self.groupkey:
           self.value = next(self.it)
           self.key = self.keyfunc(self.value)

        # 非初始状态下, self.key != self.groupkey, 所以将self.key定为self.groupkey
        self.groupkey = self.key

        # 返回: (str, generator)
        return self.key, self._grouper(self.groupkey)


def simple_test():
    text = 'AAAABBBCCDAABBB'
    ss = [(k, list(g)) for k, g in GroupBy(text)]
    assert ss == [('A', ['A', 'A', 'A', 'A']),
                  ('B', ['B', 'B', 'B']),
                  ('C', ['C', 'C']),
                  ('D', ['D']),
                  ('A', ['A', 'A']),
                  ('B', ['B', 'B', 'B'])]

    # text = ''
    # ss = [(k, list(g)) for k, g in GroupBy(text)]
    # print(ss)


def main():
    simple_test()


if __name__ == '__main__':
    main()
