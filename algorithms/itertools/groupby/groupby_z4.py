

# 07:25 - 07:30
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


# 07:33 - 07:55
def group_by(iterable):
    key = object()
    value = key
    groupkey = key

    keymap = {}
    it = iter(iterable)
    while key == groupkey:
        try:
            value = next(it)
        except StopIteration:
            return keymap
        key = value

        # 1. 当连续性中断时, 当key已存在时采取覆盖方式重构接下来的连续性.
        # 2. 当连续性中断时, 当key不存在时, 构建接下来的连续性.
        is_new_groupkey = key != groupkey
        if is_new_groupkey:
            keymap[key] = [key]
            groupkey = key
            continue

        if keymap.get(key) is None:
            keymap[key] = [key]
        else:
            keymap[key].append(key)


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


def simple_test2():
    text = 'AAAABBBCCDAABBB'
    ss = group_by(text)
    assert ss == {'C': ['C', 'C'],
                  'A': ['A', 'A'],
                  'B': ['B', 'B', 'B'],
                  'D': ['D']}


def main():
    simple_test()
    simple_test2()


if __name__ == '__main__':
    main()
