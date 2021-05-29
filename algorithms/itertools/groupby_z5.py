from typing import List, Tuple


# 06:41 - 06:44
class GroupBy:

    def __init__(self, iterable):
        self.it = iter(iterable)
        self.key = object()
        self.groupkey = self.key
        self.value = None

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


# 06:44 - 06:53
# 耗时: 9 分钟; 翻看代码两次
def group_by_1(iterable):
    it = iter(iterable)
    groupmap = {}

    key = object()
    groupkey = key
    value = None

    while True:
        try:
            value = next(it)
        except StopIteration:
            return groupmap
        key = value

        is_new_groupkey = key != groupkey
        if is_new_groupkey:
            groupkey = key
            groupmap[groupkey] = [key]
            continue

        if groupmap.get(groupkey) is None:
            groupmap[groupkey] = [key]
        else:
            groupmap[groupkey].append(key)


# 06:53 - 07:06
# 耗时: 13分钟
def group_by_2(iterable) -> List[Tuple[str, List[str]]]:
    it = iter(iterable)
    grouprst = []

    subgkey = None
    subgroup = []

    key = object()
    groupkey = key
    value = None

    while True:
        try:
            value = next(it)
        except StopIteration:

            # 尾巴处理, 将 subgkey 和 subgroup 纳入到 grouprst 中.
            tup = (subgkey, subgroup)
            grouprst.append(tup)

            return grouprst
        key = value

        is_new_groupkey = key != groupkey
        if is_new_groupkey:

            # 当 groupkey 发生变化时, 将 subgkey 和 subgroup 纳入到 grouprst 中.
            if subgkey and subgroup:
                tup = (subgkey, subgroup)
                grouprst.append(tup)

            groupkey = key
            subgkey = groupkey
            subgroup = [key]
            continue

        subgroup.append(key)


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
    assert ss == []


def simple_test2():
    text = 'AAAABBBCCDAABBB'
    ss = group_by_1(text)
    assert ss == {'C': ['C', 'C'],
                  'A': ['A', 'A'],
                  'B': ['B', 'B', 'B'],
                  'D': ['D']}


def simple_test3():
    text = 'AAAABBBCCDAABBB'
    ss = group_by_2(text)
    assert ss == [('A', ['A', 'A', 'A', 'A']),
                  ('B', ['B', 'B', 'B']),
                  ('C', ['C', 'C']),
                  ('D', ['D']),
                  ('A', ['A', 'A']),
                  ('B', ['B', 'B', 'B'])]


def main():
    simple_test()
    simple_test2()
    simple_test3()


if __name__ == '__main__':
    main()
