import sys


class MinStack:

    """
    155. 最小栈

    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

    push(x) —— 将元素 x 推入栈中。
    pop() —— 删除栈顶的元素。
    top() —— 获取栈顶元素。
    getMin() —— 检索栈中的最小元素。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/min-stack
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        """
        在入栈时，计算出一个最小值.
        在出栈时, 重新计算出一个最小值.

        push   是 O(1)
        top    是 O(1)
        getMin 是 O(1)
        pop    是 O(2n)

        最佳实践:
        https://leetcode-cn.com/problems/min-stack/comments/245076
        """
        self.min_value = sys.maxsize
        self.stack = []

    def push(self, val: int) -> None:
        self.min_value = min(val, self.min_value)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_value = sys.maxsize

        temp_stack = []
        while self.stack:
            value = self.stack.pop()
            temp_stack.append(value)
            self.min_value = min(value, self.min_value)

        while temp_stack:
            self.stack.append(temp_stack.pop())

    def top(self) -> int:
        if not self.stack: return -1
        value = self.stack.pop()
        self.stack.append(value)
        return value

    def getMin(self) -> int:
        return self.min_value


def main():
    ss = MinStack()
    x1 = ss.push(-2)
    x2 = ss.push(0)
    x3 =ss.push(-3)
    x4 = ss.getMin()
    x5 = ss.pop()
    x6 = ss.top()
    x7 = ss.getMin()
    results = [None, x1, x2, x3, x4, x5, x6, x7]
    expects = [None, None, None, None, -3, None, 0, -2]
    assert results == expects


if __name__ == '__main__':
    main()
