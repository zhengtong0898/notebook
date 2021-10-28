from typing import List


class Node:

    def __init__(self, value: str, next_node=None):
        self.value: str = value
        self.next = next_node

    def __str__(self):
        if self.next:
            return f"<Node value={self.value} next={self.next}>"
        else:
            return f"<Node value={self.value} next=''>"

    def __eq__(self, other):
        return self.value == other.value


class LinkedListSingle:

    """
    单链表

    链表特征:
    入口是一个 head_node 对象, 末端 node 的 next 是 None.

    边界问题:
    self.head       !=  None  ==  list[0]
    self.head.next  !=  None  ==  list[1]
    curr_node.next  ==  None  ==  list[-1]
    curr_node       ==  None  ==  越界: list index out of range
    """

    def __init__(self):
        self.head = Node(value="head", next_node=None)                  # 虚拟头节点

    def walk(self) -> List[str]:
        result = []
        curr_node = self.head.next                                      # 第0个节点是虚拟头节点, 所以从第1个有效节点开始遍历,
        while curr_node:                                                # 当遍历超出列表时(此时处于越界状态), 停止遍历.
            result.append(curr_node.value)
            curr_node = curr_node.next
        return result

    def find(self, value: str) -> Node:
        curr_node = self.head.next                                      # 第0个节点是虚拟头节点, 所以从第1个有效节点开始遍历,
        while curr_node:                                                # 当遍历超出列表时(此时处于越界状态), 停止遍历.
            if curr_node.value == value: return curr_node
            curr_node = curr_node.next
        return curr_node.next

    def front_insert(self, value: str):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def back_insert(self, value: str):
        curr_node = self.head                                           # 从第0个节点(虚拟头节点)开始遍历,
        while curr_node.next:                                           # 当遍历到列表最后一个元素时(没有越界), 停止遍历.
            curr_node = curr_node.next                                  # 之所以要从第0个节点开始, 是因为有可能是一个空链表,
        curr_node.next = Node(value)                                    # 当链表为空时, 将新的节点写在第1个位置处.

    def insert(self, value: str, to_index: int):
        index = 0
        curr_node = self.head                                           # 从第0个节点(虚拟头节点)开始遍历,
        while curr_node.next:                                           # 当遍历到列表最后一个元素时(没有越界), 停止遍历.
            if to_index == index: break
            curr_node = curr_node.next
            index += 1
        new_node = Node(value)
        new_node.next = curr_node.next
        curr_node.next = new_node

    def front_delete(self):
        delete_node = self.head.next
        next_node = delete_node.next
        self.head.next = next_node                                      # 解被引用, 即: 删除外部对象指向(引用)到 delete_node.
        delete_node.next = None                                         # 解引用, 即: 删除 delete_node 对外部对象的指向(引用).

    def back_delete(self):
        prev_node = self.head
        curr_node = self.head.next                                      # 从第0个节点(虚拟头节点)开始遍历,
        while curr_node.next:                                           # 当遍历到列表最后一个元素时(没有越界), 停止遍历.
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = None

    def delete(self, to_index):
        index = 0
        prev_node = self.head
        curr_node = self.head.next                                      # 从第0个节点(虚拟头节点)开始遍历,
        while curr_node.next:                                           # 当遍历到列表最后一个元素时(没有越界), 停止遍历.
            if to_index == index: break
            prev_node = curr_node
            curr_node = curr_node.next

        next_node = curr_node.next
        prev_node.next = next_node                                      # 解被引用
        curr_node.next = None                                           # 解引用


def test_llv1_walk():
    llv1 = LinkedListSingle()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.head.next.next.next = Node("c")
    llv1.head.next.next.next.next = Node("d")
    llv1.head.next.next.next.next.next = Node("e")
    ss = llv1.walk()
    assert llv1.walk() == ["a", "b", "c", "d", "e"]


def test_llv1_find():
    llv1 = LinkedListSingle()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.head.next.next.next = Node("e")
    llv1.head.next.next.next.next = Node("c")
    llv1.head.next.next.next.next.next = Node("d")
    assert llv1.find("e") == Node("e")
    assert llv1.find("d") == Node("d")
    assert llv1.find("c") == Node("c")


def test_llv1_front_insert():
    llv1 = LinkedListSingle()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.front_insert("c")
    assert llv1.head.next == Node("c")
    assert llv1.head.next.next == Node("a")
    assert llv1.head.next.next.next == Node("b")
    assert llv1.walk() == ["c", "a", "b"]


def test_llv1_back_insert():
    llv1 = LinkedListSingle()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.back_insert("c")
    assert llv1.head.next == Node("a")
    assert llv1.head.next.next == Node("b")
    assert llv1.head.next.next.next == Node("c")
    assert llv1.walk() == ["a", "b", "c"]


def test_llv1_insert():
    llv1 = LinkedListSingle()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.head.next.next.next = Node("c")
    llv1.insert(value="d", to_index=0)
    assert llv1.walk() == ["d", "a", "b", "c"]


def test_llv1_front_delete():
    llv1 = LinkedListSingle()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.head.next.next.next = Node("c")
    llv1.front_delete()
    assert llv1.walk() == ["b", "c"]
    llv1.front_delete()
    assert llv1.walk() == ["c"]
    llv1.front_delete()
    assert llv1.walk() == []


def test_llv1_back_delete():
    llv1 = LinkedListSingle()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.head.next.next.next = Node("c")
    llv1.back_delete()
    assert llv1.walk() == ["a", "b"]
    llv1.back_delete()
    assert llv1.walk() == ["a"]
    llv1.back_delete()
    assert llv1.walk() == []


def test_llv1_delete():
    llv1 = LinkedListSingle()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.head.next.next.next = Node("c")
    llv1.delete(0)
    assert llv1.walk() == ["b", "c"]
    llv1.delete(1)
    assert llv1.walk() == ["b"]


def test_llv1():
    test_llv1_walk()
    test_llv1_find()
    test_llv1_front_insert()
    test_llv1_back_insert()
    test_llv1_insert()
    test_llv1_front_delete()
    test_llv1_back_delete()
    test_llv1_delete()


def main():
    test_llv1()


if __name__ == '__main__':
    main()
