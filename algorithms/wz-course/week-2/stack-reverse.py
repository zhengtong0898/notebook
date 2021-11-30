from queue import LifoQueue


def main():
    stack = LifoQueue()
    items = ["1", "2", "3", "4", "5"]
    for i in items:
        stack.put(i)

    results = []
    for i in range(stack.qsize()):
        rightmost = stack.get()
        results.append(rightmost)

    print(results)
    assert results == ["5", "4", "3", "2", "1"]


if __name__ == '__main__':
    main()
