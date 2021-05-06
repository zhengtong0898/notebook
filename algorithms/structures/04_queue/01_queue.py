

class Queue:

    """
    这种方式的队列, 读取会很快, 移除元素很慢: O(n).
    """

    def __init__(self, max_size=10):
        self.max_size = max_size

        # None 表示: 空位置, 可再分配.
        self.queue = [None] * max_size

        self.queue_size = 0

    def size(self):
        return self.queue_size

    def __len__(self):
        return self.size()

    def front_pop(self):
        if self.size() <= 0:
            raise IndexError("can't pop empty stack.")

        # 整个列表向左移动一次
        for i in range(1, self.size()):
            self.queue[i-1] = self.queue[i]
        else:
            self.queue[i] = None

        self.queue_size -= 1

    def back_append(self, item):
        if self.size() >= self.max_size:
            raise IndexError("queue size exceeds limit.")
        self.queue[self.size()] = item
        self.queue_size += 1


def main():
    q = Queue(max_size=3)
    assert q.size() == 0
    assert q.queue == [None, None, None]
    q.back_append("a")
    q.back_append("b")
    q.back_append("c")
    assert q.queue == ["a", "b", "c"]
    q.front_pop()
    assert q.queue == ["b", "c", None]              # 所有元素向左移动一次


if __name__ == '__main__':
    main()
