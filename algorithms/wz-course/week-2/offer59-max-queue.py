from queue import Queue
from collections import deque


class MaxQueue:

    """
    剑指 Offer 59 - II. 队列的最大值

    请定义一个队列并实现函数 max_value 得到队列里的最大值，
    要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
    若队列为空，pop_front 和 max_value 需要返回 -1

    示例-1:
    输入: ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
         [[],[1],[2],[],[],[]]
    输出: [null,null,null,2,1,2]

    示例-2:
    输入: ["MaxQueue","pop_front","max_value"]
         [[],[],[]]
    输出: [null,-1,-1]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.queue = Queue()                                    # 常规队列
        self.dequeue = deque()                                  # 双向队列, 用于存放最大值队列

    def max_value(self) -> int:
        if not len(self.dequeue): return -1
        return self.dequeue[0]                                  # 双向队列, 第0个值永远是最大的值

    def push_back(self, value: int) -> None:
        self.queue.put(value)                                   # 常规队列, 常规操作

        # 假设 self.dequeue 中有两个值: [94, 16],
        # 假设 value =  89 时, 从双向队列中移除所有小于  89 的值, 然后将 value 写入到 dequeue 中, 此时的结果是: [94, 89]
        # 假设 value = 100 时, 从双向队列中移除所有小于 100 的值, 然后将 value 写入到 dequque 中, 此时的结果是: [100]
        while self.dequeue and value > self.dequeue[-1]:        # 这种操作可以被视为是均摊复杂度O(1).
            self.dequeue.pop()
        self.dequeue.append(value)

    def pop_front(self) -> int:
        if not self.queue.qsize(): return -1
        result = self.queue.get()

        # 如果移除的元素刚好是双向队列中最大的值, 则同步删除该值.
        if result == self.dequeue[0]:
            self.dequeue.popleft()

        return result


class MaxQueueV2:

    def __init__(self):
        self.queue = []
        self._max_value = -1

    def max_value(self) -> int:
        return self._max_value

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        self._max_value = max(self._max_value, value)

    def pop_front(self) -> int:
        if not len(self.queue):
            self._max_value = -1
            return self._max_value

        value = self.queue.pop(0)
        if value != self._max_value:
            return value

        self._max_value = -1
        for i in self.queue:
            self._max_value = max(i, self._max_value)
        return value



def test_1():
    ss = MaxQueue()
    x1 = ss.push_back(value=1)
    x2 = ss.push_back(value=2)
    x3 = ss.max_value()
    x4 = ss.pop_front()
    x5 = ss.max_value()
    result = [None, x1, x2, x3, x4, x5]
    expect = [None, None, None, 2, 1, 2]
    assert result == expect


def test_2():
    ss = MaxQueue()
    x1 = ss.pop_front()
    x2 = ss.max_value()
    result = [None, x1, x2]
    expect = [None, -1, -1]
    assert result == expect


def test_3():
    ss = MaxQueue()
    x1 = ss.max_value()
    x2 = ss.pop_front()
    x3 = ss.pop_front()
    x4 = ss.push_back(value=94)
    x5 = ss.push_back(value=16)
    x6 = ss.push_back(value=89)
    x7 = ss.pop_front()
    x8 = ss.push_back(22)
    x9 = ss.pop_front()
    result = [None, x1, x2, x3, x4, x5, x6, x7, x8, x9]
    expect = [None, -1, -1, -1, None, None, None, 94, None, 16]
    assert result == expect


def test_4():
    # [('MaxQueue', []), ('max_value', []), ('pop_front', []), ('max_value', []), ('push_back', [46]),
    # ('max_value', []), ('pop_front', []), ('max_value', []), ('pop_front', []), ('push_back', [868]),
    # ('pop_front', []), ('pop_front', []), ('pop_front', []), ('push_back', [525]), ('pop_front', []),
    # ('max_value', []), ('pop_front', []), ('max_value', []), ('push_back', [123]), ('push_back', [646]),
    # ('max_value', []), ('push_back', [229]), ('max_value', []), ('max_value', []), ('max_value', []),
    # ('push_back', [871]), ('pop_front', []), ('max_value', []), ('push_back', [285]), ('max_value', []),
    # ('max_value', []), ('max_value', []), ('pop_front', []), ('push_back', [45]), ('push_back', [140]),
    # ('push_back', [837]), ('push_back', [545]), ('pop_front', []), ('pop_front', []), ('max_value', []),
    # ('pop_front', []), ('pop_front', []), ('max_value', []), ('push_back', [561]), ('push_back', [237]),
    # ('pop_front', []), ('push_back', [633]), ('push_back', [98]), ('push_back', [806]), ('push_back', [717]),
    # ('pop_front', []), ('max_value', []), ('push_back', [186]), ('max_value', []), ('max_value', []),
    # ('pop_front', []), ('max_value', []), ('max_value', []), ('max_value', []), ('push_back', [268]),
    # ('pop_front', []), ('push_back', [29]), ('pop_front', []), ('max_value', []), ('max_value', []),
    # ('max_value', []), ('push_back', [866]), ('pop_front', []), ('push_back', [239]), ('push_back', [3]),
    # ('push_back', [850]), ('pop_front', []), ('max_value', []), ('pop_front', []), ('max_value', []),
    # ('max_value', []), ('max_value', []), ('pop_front', []), ('push_back', [310]), ('pop_front', []),
    # ('push_back', [674]), ('push_back', [770]), ('pop_front', []), ('push_back', [525]), ('pop_front', []),
    # ('push_back', [425]), ('pop_front', []), ('pop_front', []), ('push_back', [720]), ('pop_front', []),
    # ('pop_front', []), ('pop_front', []), ('push_back', [373]), ('push_back', [411]), ('max_value', []),
    # ('push_back', [831]), ('pop_front', []), ('push_back', [765]), ('push_back', [701]), ('pop_front', [])]
    ss = MaxQueue()
    x1 = ss.max_value()
    x2 = ss.pop_front()
    x3 = ss.max_value()
    x4 = ss.push_back(value=46)
    x5 = ss.max_value()
    x6 = ss.pop_front()
    x7 = ss.max_value()
    x8 = ss.pop_front()
    x9 = ss.push_back(868)
    x10 = ss.pop_front()
    result = [None, x1, x2, x3,   x4, x5, x6, x7, x8,   x9, x10]
    expect = [None, -1, -1, -1, None, 46, 46, -1, -1, None, 868]
    assert result == expect


def main():
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
