

# 10:54 - 10:57
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


def group_by(iterable):
    it = iter(iterable)
    result = {}

    key = object()
    groupkey = key
    value = None

    while True:
        try:
            value = next(it)
        except StopIteration:
            return result
        key = value

        is_new_groupkey = key != groupkey
        if is_new_groupkey:
            groupkey = key
            result[groupkey] = [key]
            continue

        if result.get(groupkey) is None:
            result[groupkey] = [key]
        else:
            result[groupkey].append(key)


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
