from typing import List


def cycle_list(iterable: List[str]):
    while True:
        for i in iterable:
            yield i


def simple_test():
    text = ["a", "b", "c", "d"]
    for i in cycle_list(text):
        print(i)


def main():
    simple_test()


if __name__ == '__main__':
    main()
