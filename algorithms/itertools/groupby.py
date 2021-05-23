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


class GroupBy:

    """
    __next__ 负责提取 key
    _grouper 负责按key提取value
    """

    def __init__(self, iterable, key=None):                     # 参数 key 的命名时为了与 sorted 的参数 key 命名保持一致.
        self.keyfunc = lambda x: x if key is None else key      # TODO: key使用案例, 待补充.
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()

    def __iter__(self):
        return self

    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)

    def __next__(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)
            self.currkey = self.keyfunc(self.currvalue)

        self.tgtkey = self.currkey

        return self.currkey, self._grouper(self.tgtkey)


def simple_test():
    text = 'AAAABBBCCDAABBB'
    ss = [(k, list(g)) for k, g in GroupBy(text)]
    assert ss == [('A', ['A', 'A', 'A', 'A']),
                  ('B', ['B', 'B', 'B']),
                  ('C', ['C', 'C']),
                  ('D', ['D']),
                  ('A', ['A', 'A']),
                  ('B', ['B', 'B', 'B'])]


def main():
    simple_test()


if __name__ == '__main__':
    main()
