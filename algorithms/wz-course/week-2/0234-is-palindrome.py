from typing import List
import copy


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
    给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。
    如果是，返回 true ；否则，返回 false 。

    示例-1:
    输入：head = [1,2,2,1]
    输出：true

    示例-2:
    输入：head = [1,2]
    输出：false

    https://leetcode-cn.com/problems/palindrome-linked-list/
    """

    def isPalindrome(self, head: ListNode) -> bool:
        # 将 slow 指针挪到链表中间的位置.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 将 slow 链表(slow和它后续的所有节点)反向排序
        # 特别注意:
        # 这里截断 curr_node, 也会截断 slow, 也会截断 fast, 也会截断 head
        # 截断的是slow后面的节点, 所以head被截断的也是slow后面的节点.
        reverse_node = ListNode()
        curr_node = slow
        while curr_node:
            next_node = curr_node.next
            curr_node.next = None                                   # 截断 head
            curr_node.next = reverse_node.next                      # 反向拼接
            reverse_node = ListNode(next_=curr_node)                # 反向添加
            curr_node = next_node

        # 循环比较两个节点相同则表示是回文.
        curr_node = reverse_node.next
        while curr_node:
            if curr_node.val != head.val:
                return False
            head = head.next
            curr_node = curr_node.next

        return True

    def isPalindrome_deepcopy(self, head: ListNode) -> bool:
        forward_node = ListNode()
        tail_node = forward_node

        reverse_node = ListNode()
        curr_node = head
        while curr_node:                                        # 时间复杂度 O(n)
            next_node = curr_node.next
            curr_node.next = None
            tail_node.next = copy.deepcopy(curr_node)           # 空间复杂度 O(n)
            tail_node = tail_node.next
            curr_node.next = reverse_node.next
            reverse_node = ListNode(next_=curr_node)
            curr_node = next_node

        return reverse_node.next.walk() == forward_node.next.walk()


def test_1():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ln_10.next.next = ListNode(val=3)
    ln_10.next.next.next = ListNode(val=2)
    ln_10.next.next.next.next = ListNode(val=1)
    assert Solution().isPalindrome(ln_10) is True
    # assert Solution().isPalindrome_deepcopy(ln_10) is True


def test_2():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    assert Solution().isPalindrome(ln_10) is False
    # assert Solution().isPalindrome_deepcopy(ln_10) is False


def main():
    test_1()
    test_2()


if __name__ == '__main__':
    main()
