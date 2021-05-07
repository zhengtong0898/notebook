

class Queue:

    """
    v3版本

    队列两端环接, 在数组长度不变的情况下, 插入和删除操作的最坏时间复杂度均可为O(1).
    使用这种策略, 队列元素个数最多是 max_size - 1.
    begin 指向第一个元素的前一个元素位置, 即: 如果 begin = 0, 则 第一个元素的位置 = 1.

    begin = stop 时, 队列初始化状态
    begin = stop 时, 还有另外一种情况, 即是初始化状态, 也是队列满状态, 这会导致逻辑冲突, 数据被无故覆盖.
    """

    def __init__(self, max_size=10):
        self.begin = 0
        self.stop = 0
        self.queue_size = 0
        self.max_size = max_size
        self.queue = [None] * max_size                          # None 表示: 空位置, 可再分配.

    def size(self):
        return self.queue_size

    def __len__(self):
        return self.size()

    def empty(self):
        return self.begin == self.stop                          # 根据定义, begin == stop 时, 队列为空.

    def full(self):                                             # 根据定义, 队列元素个数最多是 max_size - 1.
        return self.size() == (self.max_size - 1)

    def front_pop(self):
        if self.size() <= 0:
            raise IndexError("can't pop empty queue.")

        self.begin = (self.begin + 1) % self.max_size           # 计算环形索引
        self.queue[self.begin] = None
        self.queue_size -= 1

    def back_append(self, item):
        if self.full():
            raise IndexError("queue size exceeds limit.")

        self.stop = (self.stop + 1) % self.max_size             # 计算环形索引
        self.queue[self.stop] = item
        self.queue_size += 1


def main():
    q = Queue()

    # 测试初始化
    assert q.size() == 0
    assert q.begin == 0
    assert q.stop == 0
    assert q.full() is False
    assert q.queue == [None, None, None, None, None, None, None, None, None, None]

    q.back_append("a")
    assert q.size() == 1
    assert q.begin == 0
    assert q.stop == 1
    assert q.full() is False
    assert q.queue == [None, "a", None, None, None, None, None, None, None, None]

    q.back_append("b")
    assert q.size() == 2
    assert q.begin == 0
    assert q.stop == 2
    assert q.full() is False
    assert q.queue == [None, "a", "b", None, None, None, None, None, None, None]

    q.back_append("c")
    q.back_append("d")
    q.front_pop()
    assert q.size() == 3
    assert q.begin == 1
    assert q.stop == 4
    assert q.full() is False
    assert q.queue == [None, None, "b", "c", "d", None, None, None, None, None]

    # 填满队列右侧空槽
    q.back_append("e")
    q.back_append("f")
    q.back_append("g")
    q.back_append("h")
    q.back_append("i")
    assert q.size() == 8
    assert q.begin == 1
    assert q.stop == 9                      # 9 % 9
    assert q.full() is False
    assert q.queue == [None, None, "b", "c", "d", "e", "f", "g", "h", "i"]

    # 触发环形
    q.back_append("j")
    assert q.size() == 9
    assert q.begin == 1
    assert q.stop == 0
    assert q.full() is True
    assert q.queue == ["j", None, "b", "c", "d", "e", "f", "g", "h", "i"]

    # 触发异常: 环形策略, 队列元素个数最多是 max_size - 1.
    try:
        q.back_append("k")
    except Exception as e:
        pass
    else:
        raise IndexError("queue size exceeds limit.")

    # 移除首元素
    q.front_pop()
    assert q.size() == 8
    assert q.begin == 2
    assert q.stop == 0
    assert q.full() is False
    assert q.queue == ["j", None, None, "c", "d", "e", "f", "g", "h", "i"]


if __name__ == '__main__':
    main()

