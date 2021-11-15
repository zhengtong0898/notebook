

class MyStack:

    """
    225. 用队列实现栈

    请你仅使用两个队列实现一个后入先出（LIFO）的栈，
    并支持普通栈的全部四种操作（push、top、pop 和 empty）。

    实现 MyStack 类：
    void push(int x) 将元素 x 压入栈顶。
    int pop() 移除并返回栈顶元素。
    int top() 返回栈顶元素。
    boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

    示例-1:
    输入：["MyStack", "push", "push", "top", "pop", "empty"]
         [[], [1], [2], [], [], []]
    输出：[null, null, null, 2, 2, false]
    解释:
    MyStack myStack = new MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top(); // 返回 2
    myStack.pop(); // 返回 2
    myStack.empty(); // 返回 False

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/implement-stack-using-queues
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        """
        约束: 为了方便起见, 暂用 List 代替 Queue,
        同时由于队列只能FIFO, 在当前例子的后续的代码中只能使用 append 和 pop(0) 操作.

            初始场景               第一步               第二步              第三步              第四步
        _______  _______    _______  _______    _______  _______    _______  _______    _______  _______
        |  3  |  |     |    |     |  |     |    |     |  |     |    |     |  |     |    |     |  |     |
        _______  _______    _______  _______    _______  _______    _______  _______    _______  _______
        |  2  |  |     |    |  3  |  |     |    |     |  |  2  |    |     |  |     |    |  2  |  |     |
        _______  _______    _______  _______    _______  _______    _______  _______    _______  _______
        |  1  |->|     |    |  2  |->|  1  |    |  3  |  |  1  |    |  1  |<-|  2  |    |  1  |  |     |
        _______  _______    _______  _______    _______  ------     _______  _______    _______  _______
                                                   |
                                                   v
                                                remove
        """
        self._top = None
        self.queue_a = []
        self.queue_b = []

    def push(self, x: int) -> None:
        self._top = x
        self.queue_a.append(x)

    def pop(self) -> int:
        return_value = None
        while self.queue_a:
            value = self.queue_a.pop(0)
            if not len(self.queue_a):
                return_value = value
            else:
                self.queue_b.append(value)

        while self.queue_b:
            value = self.queue_b.pop(0)
            self.queue_a.append(value)
            self._top = value

        return return_value

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return not bool(self.queue_a)


def main():
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.pop()
    param_4 = obj.pop()
    param_5 = obj.empty()
    print("sss")


if __name__ == '__main__':
    main()
