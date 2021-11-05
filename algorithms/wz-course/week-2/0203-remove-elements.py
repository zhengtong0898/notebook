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
    给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

    https://leetcode-cn.com/problems/remove-linked-list-elements/
    """

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        改变链表的万能写法

        创建一个新的链表头节点, 将不等于 val 的节点, back_append 到新的链表头节点中.
        """
        head_node = ListNode()
        tail_node = head_node
        curr_node = head

        while curr_node:

            if curr_node.val == val:
                curr_node = curr_node.next          # 切换到下一个节点
                continue

            next_node = curr_node.next              # curr_node 链条切换节点-1: 先将下一个节点取出来
            curr_node.next = None                   # curr_node 链条解引用, 将链条截断后变成单一的节点.
            tail_node.next = curr_node              # tail_node 链条 back_append 尾部添加 curr_node 这个单一节点.
            tail_node = tail_node.next              # tail_node 链条切换到下一个节点(时刻都要处于链表的尾部).
            curr_node = next_node                   # curr_node 链条切换节点-2: 切换到下一个节点

        return head_node.next

    def removeElements_v2(self, head: ListNode, val: int) -> ListNode:
        """
        遍历链表, 将等于 val 的节点链接解除, 并重新链接到下一个节点.

        这段代码并不能通过 leet-code 的测试.
        """
        prev_node = ListNode(next_=head)
        curr_node = head
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next     # prev_node 直接与下下个节点进行链接, 同时 prev_node 不切换到下一个节点.
                curr_node = curr_node.next          # curr_node 切换到下一个节点.
                continue

            prev_node = prev_node.next
            curr_node = curr_node.next
        return head


def main():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ln_10.next.next = ListNode(val=6)
    ln_10.next.next.next = ListNode(val=3)
    ln_10.next.next.next.next = ListNode(val=4)
    ln_10.next.next.next.next.next = ListNode(val=5)
    ln_10.next.next.next.next.next.next = ListNode(val=6)
    assert ln_10.walk() == [1, 2, 6, 3, 4, 5, 6]
    ss = Solution().removeElements(ln_10, 6)
    assert ss.walk() == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    main()
