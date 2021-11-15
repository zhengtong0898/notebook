

class CQueue:

    """
    剑指 Offer 09. 用两个栈实现队列

    用两个栈实现一个队列(FIFO)。

    队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
    分别完成在队列尾部插入整数和在队列头部删除整数的功能。
    (若队列中没有元素，deleteHead 操作返回 -1 )

    示例-1:
    输入：["CQueue","appendTail","deleteHead","deleteHead"]
         [[],[3],[],[]]
    输出：[null,null,3,-1]

    示例-2:
    输入：["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
         [[],[],[5],[2],[],[]]
    输出：[null,-1,null,null,5,2]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        """
        关键约束: Python 没有 Stack 对象, 所以暂用 List 代替,
        同时由于栈只能LIFO, 在当前例子的后续的代码中只能使用 append 和 pop() 操作.

        解题思路:
        使用类似于汉诺塔的方式, 如果要挪动底部元素，则需要现将底部元素挨个挪到旁边，才能操作底部元素.
        栈-1: [1, 2, 3, 4, 5]
        栈-2: []
        假设如果要删除栈-1的底部元素,
        则需要先将 2, 3, 4, 5 全部移动栈-2;                此时 栈-1 的数据是: [],            栈-2 的数据是: [5, 4, 3, 2, 1]
        然后删除栈-1底部的1;                              此时 栈-1 的数据是: [],            栈-2 的数据是: [5, 4, 3, 2]
        最后将栈-2的数据挪回栈-1;                          此时 栈-1 的数据是: [2, 3, 4, 5],  栈-2 的数据是: []

        其他办法:
        这里采取的是: 在添加元素时简单, 在删除时捣腾.
        还有另外一种方式是反过来的, 在添加元素时捣腾, 在删除时简单.
        """
        self.stack_a = []
        self.stack_b = []

    def appendTail(self, value: int) -> None:
        self.stack_a.append(value)

    def deleteHead(self) -> int:
        if not self.stack_a: return -1

        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())

        return_value = self.stack_b.pop()

        while self.stack_b:
            self.stack_a.append(self.stack_b.pop())

        return return_value


class DQueue:

    def __init__(self):
        """
        这里采取的是: 在添加元素时捣腾, 在删除时简单.
        """
        self.stack_a = []
        self.stack_b = []

    def appendTail(self, value: int) -> None:
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())

        self.stack_a.append(value)

        while self.stack_b:
            self.stack_a.append(self.stack_b.pop())

    def deleteHead(self) -> int:
        if not self.stack_a: return -1
        return self.stack_a.pop()


def main():
    obj = CQueue()
    obj.deleteHead()
    obj.appendTail(5)
    obj.appendTail(2)
    obj.deleteHead()
    obj.deleteHead()


if __name__ == '__main__':
    main()
