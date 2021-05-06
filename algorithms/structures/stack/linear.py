

class StackLinear:

    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def size(self):
        return self.__len__()

    def pop(self):
        if self.size() <= 0:
            raise IndexError("can't pop empty stack.")
        return self.stack.pop()

    def append(self, item):
        self.stack.append(item)

def test_1():

    stack_linear = StackLinear()
    stack_linear.append("first")                        # 从 栈顶部(右侧) 添加元素
    stack_linear.append("second")
    assert stack_linear.size() == 2                     # 获取 栈 元素总数.
    assert len(stack_linear) == 2                       # 获取 栈 元素总数.
    last_item = stack_linear.pop()                      # 从 栈顶部(右侧) 移除元素
    assert last_item == "second"


def main():

    test_1()


if __name__ == '__main__':
    main()


