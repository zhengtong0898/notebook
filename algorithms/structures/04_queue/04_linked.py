

class Node:

    def __init__(self, value, next_to=None):
        self.value = value
        self.next = next_to

    def __eq__(self, other):
        if self.value == other.value:
            return True


class QueueLinked:

    def __init__(self, max_size=10):
        self.begin = None
        self.stop = None
        self.queue_size = 0
        self.max_size = 10

    def size(self):
        return self.queue_size

    def __len__(self):
        return self.size()

    def empty(self):
        return self.queue_size == 0 and self.begin is None

    def full(self):
        return self.max_size == self.queue_size

    def front_pop(self):
        if self.empty():
            raise IndexError("can't pop empty queue.")

        # 先将非 top_node 全部取出来, 保留引用
        temp_node = self.begin.next

        # 解引用(.next), 执行移除动作.
        return_node = self.begin
        return_node.next = None

        # 将非 top_node 复制给 self.begin, 即: 已完成移除动作.
        self.begin = temp_node
        self.queue_size -= 1

        if return_node == self.stop:
            self.stop = None

        # 返回移除对象.
        return return_node

    def back_append(self, item):
        if self.full():
            raise IndexError("queue size exceeds limit.")

        back_node = Node(item)

        # 队列为空, 首次插入元素
        if self.empty():
            self.begin = back_node
            self.stop = back_node

        # 队列非空.
        if not self.empty():
            # 当第二次插入元素时, 由于 self.stop == self.begin, 即: 上一次的 back_node 有两次引用.
            # 当执行 self.stop.next = back_node, 实际上会作用在 self.begin 和 self.stop 两个对象上.
            # 当执行 self.stop = back_node 后, self.begin != self.stop, 但 self.begin.next == self.stop.
            #
            # 当第三次插入元素时, 由于 self.begin.next == self.stop, 即: 上一次的 back_node 有两次引用.
            # 当执行 self.stop.next = back_node, 实际上会作用在 self.begin.next 和 self.stop 两个对象上.
            # 当执行 self.stop = back_node 后, self.begin.next != self.stop, 但 self.begin.next.next == self.stop.
            #
            # 以此类推.
            self.stop.next = back_node
            self.stop = back_node

        self.queue_size += 1


def main():
    ql = QueueLinked()
    ql.back_append("10")
    ql.back_append("20")
    ql.back_append("30")
    assert ql.size() == 3
    assert ql.begin.value == "10"
    assert ql.begin.next.value == "20"
    assert ql.begin.next.next.value == "30"
    assert ql.begin.next.next.next is None

    ss = ql.front_pop()
    assert ql.size() == 2
    assert ss == Node("10")
    assert ss.value == "10"
    assert ql.begin.value == "20"
    assert ql.begin.next.value == "30"
    assert ql.begin.next.next is None

    ss_1 = ql.front_pop()
    ss_2 = ql.front_pop()
    assert ql.size() == 0
    assert ss_1 == Node("20")
    assert ss_1.value == "20"
    assert ss_2 == Node("30")
    assert ss_2.value == "30"
    assert ql.begin is None
    assert ql.stop is None

    try:
        ql.front_pop()
    except Exception as e:
        pass
    else:
        raise IndexError("can't pop empty queue.")

    ql.back_append("hello")
    assert ql.size() == 1
    assert ql.begin == Node("hello")
    assert ql.stop == Node("hello")


if __name__ == '__main__':
    main()

