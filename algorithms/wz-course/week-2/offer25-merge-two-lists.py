from typing import List


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return f"<{self.__class__.__name__} val={self.val} next={self.next} >"

    def walk(self) -> List[int]:
        result = []
        curr_node = self
        while curr_node:
            result.append(curr_node.val)
            curr_node = curr_node.next
        return result


class Solution:

    """
    输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

    示例1：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4

    https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        遍历三要素

        指针初始值:      l1, l2;                             # 在同一个赛道上;
        遍历的结束条件:   l1 is None or                       # 当左链表是None时，表示右链表可以直接链接在左表的next位置
                        l2 is None                          # 当右链表是None时，表示左链表可以直接链接在右表的next位置
        遍历的核心逻辑:   ...

        """
        head = ListNode()
        tail = head
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next

        if l1 is None:
            tail.next = l2
        else:
            tail.next = l1

        return head.next


def test_1():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=3)
    ln_10.next.next = ListNode(val=5)

    ln_20 = ListNode(val=2)
    ln_20.next = ListNode(val=6)
    ln_20.next.next = ListNode(val=8)

    ss = Solution().mergeTwoLists(ln_10, ln_20)
    assert ss.walk() == [1, 2, 3, 5, 6, 8]


def test_2():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ln_10.next.next = ListNode(val=4)

    ln_20 = ListNode(val=1)
    ln_20.next = ListNode(val=3)
    ln_20.next.next = ListNode(val=4)

    ss = Solution().mergeTwoLists(ln_10, ln_20)
    xx = ss.walk()
    assert ss.walk() == [1, 1, 2, 3, 4, 4]


def main():
    test_1()
    test_2()


if __name__ == '__main__':
    main()
