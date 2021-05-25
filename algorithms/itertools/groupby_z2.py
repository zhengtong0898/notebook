# 10:28 - 10:33


class GroupBy:

    def __init__(self, iterable):
        self.it = iter(iterable)
        self.key = self.value = self.groupkey = object()

    def __iter__(self):
        return self

    def __next__(self):
        while self.key == self.groupkey:
            self.value = next(self.it)
            self.key = self.value
        self.groupkey = self.key
        return self.groupkey, self.grouper()

    def grouper(self):
        while self.key == self.groupkey:
            yield self.value
            try:
                self.value = next(self.it)
            except StopIteration:
                return
            self.key = self.value



def simple_test():
    text = 'AAAABBBCCDAABBB'
    ss = [(k, list(g)) for k, g in GroupBy(text)]
    assert ss == [('A', ['A', 'A', 'A', 'A']),
                  ('B', ['B', 'B', 'B']),
                  ('C', ['C', 'C']),
                  ('D', ['D']),
                  ('A', ['A', 'A']),
                  ('B', ['B', 'B', 'B'])]

    text = ''
    ss = [(k, list(g)) for k, g in GroupBy(text)]
    print(ss)


def main():
    simple_test()


if __name__ == '__main__':
    main()
