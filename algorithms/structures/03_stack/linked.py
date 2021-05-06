

class Node:

    def __init__(self, value, next_to=None):
        self.value = value
        self.next = next_to

    def __eq__(self, other):
        if self.value == other.value:
            return True


class StackLinked:

    def __init__(self):
        self.top_node = None
        self.node_size = 0

    def size(self):
        return self.node_size

    def __len__(self):
        return self.size()

    def append(self, value):
        top_node = Node(value, next_to=self.top_node)
        self.top_node = top_node
        self.node_size += 1

    def pop(self):
        if self.node_size == 0:
            raise IndexError("can't pop empty stack.")

        temp_node = self.top_node.next                  # 先将非 top_node 全部取出来, 复制给 temp_node 临时变量,
                                                        # 作用: 保留引用, 避免被垃圾回收.

        return_node = self.top_node                     # 将 top_node 复制给 return_node 临时变量, 并将 .next 置空.
        return_node.next = None                         # 通过这种方式, 解引用(.next).

        self.top_node = temp_node                       # 将 temp_node 作为 top_node 对象, 即: 移除了原来的 top_node.
        self.node_size -= 1
        return return_node


def test_1():

    stack_linear = StackLinked()
    stack_linear.append("first")                        # 从 链表顶部 添加元素
    stack_linear.append("second")
    stack_linear.append("third")
    assert stack_linear.size() == 3                     # 获取 链表 元素总数.
    assert len(stack_linear) == 3                       # 获取 链表 元素总数.
    last_item = stack_linear.pop()                      # 从 链表顶部 移除元素
    assert last_item == Node("third")


def main():

    test_1()


if __name__ == '__main__':
    main()

