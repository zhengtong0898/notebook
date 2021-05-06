

class Queue:

    """
    v2版本

    每次删除一个队列元素时, 不需要把剩下的元素左移一个位置,
    只需要简单的把 begin(队首元素) 加 1 即可(也被称为: begin 右移一个位置),
    stop(末尾元素)位置不变.

    每次添加一个队列元素时, begin位置不变, stop位置右移一个位置.

    多次删除动作(begin多次右移) + 多次添加动作(stop多次右移), 会出现一种情况, 即:
    stop已经抵达队列长度的最后一个位置, 无法继续添加元素, 但是 begin 左侧还有空位置没使用.
    当出现这种情况时, 整体元素需要向左移动, 每个元素都需要向左移动(begin - 1)个位置.

    备注: 没使用锁, 不支持并发.
    """

    def __init__(self, max_size=10):
        self.begin = 0
        self.stop = 0
        self.queue_size = 0
        self.max_size = max_size
        self.queue = [None] * max_size                  # None 表示: 空位置, 可再分配.

    def size(self):
        return self.queue_size

    def __len__(self):
        return self.size()

    def front_pop(self):
        if self.size() <= 0:
            raise IndexError("can't pop empty queue.")

        self.queue[self.begin] = None
        self.begin += 1
        self.queue_size -= 1

    def append(self, item):
        if self.size() >= self.max_size:
            raise IndexError("queue size exceeds limit.")

        freebegin = self.begin > 0
        endpos = self.stop >= self.max_size
        if freebegin and endpos:
            self._move_to_begin()

        self.queue[self.stop] = item
        self.stop += 1
        self.queue_size += 1

    def _move_to_begin(self):
        """ 元素整体向左移动 """

        # 左移
        for i in range(self.begin, self.stop):
            offset = i - self.begin
            self.queue[offset] = self.queue[i]

        # 右侧置空
        for i in range(1, self.begin + 1):
            self.queue[-i] = None

        self.stop = self.stop - self.begin
        self.begin = 0


def main():

    q = Queue()

    # 测试初始化
    assert q.size() == 0
    assert q.begin == 0
    assert q.stop == 0
    assert q.queue == [None, None, None, None, None, None, None, None, None, None]

    # 测试插入
    q.append("a")
    q.append("b")
    q.append("c")
    q.append("d")
    q.append("e")
    assert q.size() == 5
    assert q.begin == 0
    assert q.stop == 5
    assert q.queue == ["a", "b", "c", "d", "e", None, None, None, None, None]

    # 测试单次移除
    q.front_pop()
    assert q.size() == 4
    assert q.begin == 1
    assert q.stop == 5
    assert q.queue == [None, "b", "c", "d", "e", None, None, None, None, None]

    # 测试多次移除, 多次添加(到末端)
    q.front_pop()
    q.front_pop()
    q.append("v")
    q.append("w")
    q.append("x")
    q.append("y")
    q.append("z")
    assert q.size() == 4 - 2 + 5
    assert q.begin == 3
    assert q.stop == 10
    assert q.queue == [None, None, None, "d", "e", "v", "w", "x", "y", "z"]

    # 再次添加, 触发整体向左移动到队首.
    q.append("hello")
    assert q.size() == 8
    assert q.begin == 0
    assert q.stop == 8
    assert q.queue == ["d", "e", "v", "w", "x", "y", "z", "hello", None, None]

    # 全部置空
    q.front_pop()
    q.front_pop()
    q.front_pop()
    q.front_pop()
    q.front_pop()
    q.front_pop()
    q.front_pop()
    q.front_pop()
    assert q.size() == 0
    assert q.begin == 8
    assert q.stop == 8
    assert q.queue == [None, None, None, None, None, None, None, None, None, None]

    try:
        q.front_pop()
    except Exception as e:
        pass                                            # 期望是报错
    else:
        raise IndexError("can't pop empty queue.")


if __name__ == '__main__':
    main()

