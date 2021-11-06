# 循环链表
# 首先, 循环链表并不是一个特定的数据结构,
# 它是链表中的一种表现, 即: 尾节点.next指向头节点.
#
# 使用场景:
# 音乐播放器的循环播放.
#
# 注意事项:
# 当 ListNode.next 是 None 时，它是一个单节点.
# 当 ListNode.next 非 None 时，并且尾节点是 None  时，它是一个普通链表。
# 当 ListNode.next 非 None 时，并且尾节点是 头节点 时，它是一个循环链表。
#
# 循环链表需要具备的方法:
# back_append: 需要将 尾节点.next 断开, 然后写入新的节点, 嘴周将 .next 衔接回来.
# is_cycle: 判断一个链表是不是循环链表.
from typing import List


class ListNode:

    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return f"{self.walk()}"

    def walk(self) -> List[int]:
        """
        遍历链表
        """
        result = []
        curr_node = self
        while curr_node:
            result.append(curr_node.val)
            if curr_node.next == self:
                return result
            curr_node = curr_node.next              # 右移一位
        return result

    def is_cycle(self):
        curr_node = self
        while curr_node:
            if curr_node.next == self:
                return True
            curr_node = curr_node.next              # 右移一位
        return False

    def back_append(self, node):
        """ 前提条件: self是一个循环链表 """
        curr_node = self
        while curr_node:
            if curr_node.next is self:
                break
            curr_node = curr_node.next
        node.next = curr_node.next                  # 节点交换
        curr_node.next = node                       # 节点交换


def test_is_cycle():
    ln = ListNode(val=1)
    ln.next = ListNode(val=2)
    ln.next.next = ListNode(val=3)
    assert ln.is_cycle() is False
    ln.next.next.next = ln
    assert ln.is_cycle() is True


def test_back_append():
    ln = ListNode(val=1)
    ln.next = ListNode(val=2)
    ln.next.next = ListNode(val=3)
    ln.next.next.next = ln
    ln.back_append(ListNode(val=4))
    ln.back_append(ListNode(val=5))
    ln.back_append(ListNode(val=7))
    ln.back_append(ListNode(val=6))
    assert ln.is_cycle() is True


def main():
    test_is_cycle()
    test_back_append()


if __name__ == '__main__':
    main()

