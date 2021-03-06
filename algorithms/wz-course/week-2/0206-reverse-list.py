from typing import List


class ListNode:

    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return f"{self.walk()}"

    def walk(self) -> List[int]:
        result = []
        curr_node = self
        while curr_node:
            result.append(curr_node.val)
            curr_node = curr_node.next
        return result


class Solution:

    """
    给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

    示例-1:
    输入: [1, 2, 3, 4, 5]
    输出: [5, 4, 3, 2, 1]

    示例-2:
    输入: [1, 2]
    输出: [2, 1]

    https://leetcode-cn.com/problems/reverse-linked-list/
    """

    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None                                # "上一个"指针节点
        curr_node = head                                # 当前指针节点
        while curr_node:                                                                             # 时间复杂度 O(n)
            next_node = curr_node.next                  # 创建临时变量保存"下一个节点"
            curr_node.next = prev_node                  # 截断 curr_node 链表, 将"上一个"节点, 链接到此处.
            prev_node = curr_node                       # 将 curr_node 存放在 prev_node 中.
            curr_node = next_node                       # curr_node 向右移动一位.
        return prev_node

    def reverseList_v2(self, head: ListNode) -> ListNode:
        if not head: return head
        rst_node = ListNode()
        while head:                                                                                  # 时间复杂度 O(n)
            head_next = head.next                       # 创建临时变量保存 head 链表的后续节点
            head.next = None                            # 截断 head 链表, 使其变成一个 "尾节点" 状态
            head.next = rst_node.next                   # 将 rst_node 链表的所有节点，对接到 head 链表
            rst_node = ListNode(next_=head)             # 将 rst_node 向左移动一位                       空间复杂度 O(n)
            head = head_next                            # head 向右移动一位
        return rst_node.next


def test_1():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ln_10.next.next = ListNode(val=3)
    ln_10.next.next.next = ListNode(val=4)
    ln_10.next.next.next.next = ListNode(val=5)
    ss = Solution().reverseList(ln_10)
    xx = ss.walk()
    assert xx == [5, 4, 3, 2, 1]


def test_2():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ss = Solution().reverseList(ln_10)
    xx = ss.walk()
    assert xx == [2, 1]


def main():
    test_1()
    test_2()


if __name__ == '__main__':
    main()
