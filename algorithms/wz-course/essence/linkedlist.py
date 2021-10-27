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


class LinkedListV1:

    """
    单链表

    链表特征是入口是一个 head_node对象, 末端 node 的 next 是 None.
    """

    def __init__(self):
        self.head = Node(value="head", next_node=None)                  # 虚拟头节点

    def walk(self) -> List[str]:
        """
        边界: 从 self.head.next 开始, 到 curr_node == None 结束; 等同于:
             range(1, 10+1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        result = []
        curr_node = self.head.next
        while curr_node:
            result.append(curr_node.value)
            curr_node = curr_node.next
        return result

    def find(self, value: str) -> Node:
        """
        range(1, 10+1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        curr_node = self.head.next
        while curr_node:
            if curr_node.value == value: return curr_node
            curr_node = curr_node.next
        return curr_node.next

    def front_insert(self, value: str):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def back_insert(self, value: str):
        """
        range(0, 10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(value)

    def insert(self, value: str, to_index: int):
        """
        range(0, 10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        index = 0
        curr_node = self.head
        while curr_node.next:
            if to_index == index: break
            curr_node = curr_node.next
            index += 1
        new_node = Node(value)
        new_node.next = curr_node.next
        curr_node.next = new_node

    def front_delete(self):
        delete_node = self.head.next
        next_node = delete_node.next
        self.head.next = next_node          # 解被引用, 即: 删除外部对象指向(引用)到 delete_node.
        delete_node.next = None             # 解引用, 即: 删除 delete_node 对外部对象的指向(引用).

    def back_delete(self):
        """
        range(0, 10+1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        prev_node = self.head
        curr_node = self.head.next
        while curr_node.next:
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = None

    def delete(self, to_index):
        """
        range(0, 10+1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        index = 0
        prev_node = self.head
        curr_node = self.head.next
        while curr_node.next:
            if to_index == index: break
            prev_node = curr_node
            curr_node = curr_node.next

        next_node = curr_node.next
        prev_node.next = next_node          # 解被引用
        curr_node.next = None               # 解引用


def test_llv1_walk():
    llv1 = LinkedListV1()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.head.next.next.next = Node("c")
    llv1.head.next.next.next.next = Node("d")
    llv1.head.next.next.next.next.next = Node("e")
    ss = llv1.walk()
    assert llv1.walk() == ["a", "b", "c", "d", "e"]


def test_llv1_find():
    llv1 = LinkedListV1()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.head.next.next.next = Node("e")
    llv1.head.next.next.next.next = Node("c")
    llv1.head.next.next.next.next.next = Node("d")
    assert llv1.find("e") == Node("e")
    assert llv1.find("d") == Node("d")
    assert llv1.find("c") == Node("c")


def test_llv1_front_insert():
    llv1 = LinkedListV1()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.front_insert("c")
    assert llv1.head.next == Node("c")
    assert llv1.head.next.next == Node("a")
    assert llv1.head.next.next.next == Node("b")
    assert llv1.walk() == ["c", "a", "b"]


def test_llv1_back_insert():
    llv1 = LinkedListV1()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.back_insert("c")
    assert llv1.head.next == Node("a")
    assert llv1.head.next.next == Node("b")
    assert llv1.head.next.next.next == Node("c")
    assert llv1.walk() == ["a", "b", "c"]


def test_llv1_insert():
    llv1 = LinkedListV1()
    llv1.head.next = Node("a")
    llv1.head.next.next = Node("b")
    llv1.head.next.next.next = Node("c")
    llv1.insert(value="d", to_index=0)
    assert llv1.walk() == ["d", "a", "b", "c"]


def test_llv1_front_delete():
    llv1 = LinkedListV1()
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
    llv1 = LinkedListV1()
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
    llv1 = LinkedListV1()
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
