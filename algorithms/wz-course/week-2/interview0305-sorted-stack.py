

class SortedStack:

    """
    面试题 03.05. 栈排序

    编写程序，对栈进行排序使最小元素位于栈顶。
    最多只能使用一个其他的临时栈存放数据，
    但不得将元素复制到别的数据结构（如数组）中。
    该栈支持如下操作：push、pop、peek 和 isEmpty。
    当栈为空时，peek 返回 -1。

    示例-1:
    输入: ["SortedStack", "push", "push", "peek", "pop", "peek"]
          [[], [1], [2], [], [], []]
    输出: [None,None,None,1,None,2]


    示例-2:
     输入: ["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
           [[], [], [], [1], [], []]
     输出: [None,None,None,None,None,True]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/sort-of-stacks-lcci
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        """
        约束: 为了方便起见, 暂用 List 代替 Queue,
        同时由于栈只能LIFO, 在当前例子的后续的代码中只能使用 append 和 pop() 操作.

        题目说对栈进行排序, 这通常是在写入时完成排序;
        """
        self.stack_a = []
        self.stack_b = []

    def push(self, val: int) -> None:
        if not self.stack_a:
            self.stack_a.append(val)
            return

        inserted = False
        while self.stack_a:
            a_val = self.stack_a.pop()
            if not inserted and val < a_val:
                inserted = True
                self.stack_b.append(val)
            self.stack_b.append(a_val)

        if not inserted:
            self.stack_b.append(val)

        while self.stack_b:
            b_val = self.stack_b.pop()
            self.stack_a.append(b_val)

    def pop(self) -> None:
        if self.stack_a:
            self.stack_a.pop()

    def peek(self) -> int:
        if not self.stack_a: return -1
        value = self.stack_a.pop()
        self.stack_a.append(value)
        return value

    def isEmpty(self) -> bool:
        return not bool(self.stack_a)


# Your SortedStack object will be instantiated and called as such:
def test_1():
    obj = SortedStack()
    obj.push(1)
    obj.push(2)
    a = obj.peek()
    b = obj.pop()
    c = obj.peek()


def test_2():
    """
    ["SortedStack",         []                                      ss
     "peek",                []                                      x1
     "peek",                []                                      x2
     "pop",                 []                                      x3
     "isEmpty",             []                                      x4
     "peek",                []                                      x5
     "push",                [40]                                    x6
     "pop",                 []                                      x7
     "push",                [19]                                    x8
     "peek",                []                                      x9
     "push",                [44]                                    x10
     "peek",                []                                      x11
     "pop",                 []                                      x12
     "pop",                 []                                      x13
     "push",                [42]                                    x14
     "isEmpty",             []                                      x15
     "push",                [8]                                     x16
     "peek",                []                                      x17
     "isEmpty",             []                                      x18
     "push",                [29]                                    x19
     "peek",                []                                      x20
     "peek",                []                                      x21
     "isEmpty",             []                                      x22
     "push",                [25]                                    x23
     "isEmpty",             []                                      x24
     "peek",                []                                      x25
     "isEmpty",             []                                      x26
     "pop",                 []                                      x27
     "peek",                []                                      x28
     "pop",                 []                                      x29
     "push",                [52]                                    x30
     "push",                [63]                                    x31
     "isEmpty",             []                                      x32
     "pop",                 []                                      x33
     "isEmpty",             []                                      x34
     "peek",                []                                      x35
     "push",                [47]                                    x36
     "pop",                 []                                      x37
     "push",                [45]                                    x38
     "push",                [52]                                    x39
     "isEmpty",             []                                      x40
     "pop",                 []                                      x41
     "pop",                 []                                      x42
     "push",                [17]                                    x43
     "peek",                []                                      x44
     "isEmpty",             []                                      x45
     "pop",                 []                                      x46
     "peek",                []                                      x47
     "push",                [6]                                     x48
     "push",                [30]                                    x49
     "peek",                []                                      x50
     "isEmpty",             []                                      x51
     "isEmpty",             []                                      x52
     "isEmpty",             []                                      x53
     "isEmpty",             []                                      x54
     "isEmpty",             []                                      x55
     "push",                [51]                                    x56
     "push",                [46]                                    x57
     "push",                [2]                                     x58
     "push",                [56]                                    x59
     "push",                [39]                                    x60
     "peek",                []                                      x61
     "peek",                []                                      x62
     "isEmpty",             []                                      x63
     "push"]                [38]                                    x64
    """
    ss = SortedStack()
    x1 = ss.peek()
    x2 = ss.peek()
    x3 = ss.pop()
    x4 = ss.isEmpty()
    x5 = ss.peek()
    x6 = ss.push(40)
    x7 = ss.pop()
    x8 = ss.push(19)
    x9 = ss.peek()
    x10 = ss.push(44)
    x11 = ss.peek()
    x12 = ss.pop()
    x13 = ss.pop()
    x14 = ss.push(42)
    x15 = ss.isEmpty()
    x16 = ss.push(8)
    x17 = ss.peek()
    x18 = ss.isEmpty()
    x19 = ss.push(29)
    x20 = ss.peek()
    x21 = ss.peek()
    x22 = ss.isEmpty()
    x23 = ss.push(25)
    x24 = ss.isEmpty()
    x25 = ss.peek()
    x26 = ss.isEmpty()
    x27 = ss.pop()
    x28 = ss.peek()
    x29 = ss.pop()
    x30 = ss.push(52)
    x31 = ss.push(63)
    x32 = ss.isEmpty()
    x33 = ss.pop()
    x34 = ss.isEmpty()
    x35 = ss.peek()
    x36 = ss.push(47)
    x37 = ss.pop()
    x38 = ss.push(45)
    x39 = ss.push(52)
    x40 = ss.isEmpty()
    x41 = ss.pop()
    x42 = ss.pop()
    x43 = ss.push(17)
    x44 = ss.peek()
    x45 = ss.isEmpty()
    x46 = ss.pop()
    x47 = ss.peek()
    x48 = ss.push(6)
    x49 = ss.push(30)
    x50 = ss.peek()
    x51 = ss.isEmpty()
    x52 = ss.isEmpty()
    x53 = ss.isEmpty()
    x54 = ss.isEmpty()
    x55 = ss.isEmpty()
    x56 = ss.push(51)
    x57 = ss.push(46)
    x58 = ss.push(2)
    x59 = ss.push(56)
    x60 = ss.push(39)
    x61 = ss.peek()
    x62 = ss.peek()
    x63 = ss.isEmpty()
    x64 = ss.push(38)
    result = [None, x1, x2, x3, x4, x5, x6, x7, x8, x9,
              x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
              x20, x21, x22, x23, x24, x25, x26, x27, x28, x29,
              x30, x31, x32, x33, x34, x35, x36, x37, x38, x39,
              x40, x41, x42, x43, x44, x45, x46, x47, x48, x49,
              x50, x51, x52, x53, x54, x55, x56, x57, x58, x59,
              x60, x61, x62, x63, x64]
    expect = [None, -1, -1, None, True, -1, None, None, None, 19,
              None, 19, None, None, None, False, None, 8, False, None,
              8, 8, False, None, False, 8, False, None, 25, None,
              None, None, False, None, False, 42, None, None, None, None,
              False, None, None, None, 17, False, None, 52, None, None,
              6, False, False, False, False, False, None, None, None, None,
              None, 2, 2, False, None]
    assert result == expect


def test_3():

    ss = SortedStack()              # "SortedStack"
    x1 = ss.peek()                  # "peek"
    x2 = ss.isEmpty()               # "isEmpty"
    x3 = ss.peek()                  # "peek"
    x4 = ss.push(18)                # "push"            18
    x5 = ss.isEmpty()               # "isEmpty"
    x6 = ss.peek()                  # "peek"
    x7 = ss.pop()                   # "pop"
    x8 = ss.push(40)                # "push"            40
    x9 = ss.isEmpty()               # "isEmpty"
    x10 = ss.peek()                 # "peek"
    x11 = ss.push(12)               # "push"            12
    x12 = ss.push(3)                # "push"            3
    x13 = ss.push(38)               # "push"            38
    x14 = ss.isEmpty()              # "isEmpty"
    x15 = ss.isEmpty()              # "isEmpty"
    x16 = ss.peek()                 # "peek"
    x17 = ss.peek()                 # "peek"
    x18 = ss.pop()                  # "pop"
    x19 = ss.peek()                 # "peek"
    x20 = ss.pop()                  # "pop"
    x21 = ss.pop()                  # "pop"
    x22 = ss.pop()                  # "pop"
    x23 = ss.peek()                 # "peek"

    result = [None, x1, x2, x3, x4, x5, x6, x7, x8, x9,
              x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
              x20, x21, x22, x23]
    expect = [None, -1, True, -1, None, False, 18, None, None, False,
              40, None, None, None, False, False, 3, 3, None, 12,
              None, None, None, -1]
    assert result == expect


def main():
    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    main()
