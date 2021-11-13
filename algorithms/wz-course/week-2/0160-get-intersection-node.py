from typing import List, Optional


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
    160. 相交链表

    给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

    示例-1:
    输入：listA = [4, 1, 8, 4, 5],
         listB = [5, 0, 1, 8, 4, 5]
    输出：[8, 4, 5]
    注意: 为什么 listA 的 1，和 ListB 的 1 不是相交节点?
         因为这里强调的是相同的节点相交，不是值相同的节点相交.

    示例-2:
    输入: listA = [0, 9, 1, 2, 4],
         listB = [3, 2, 4]
    输出: [2, 4]

    示例-3:
    输入: listA = [2,6,4],
         listB = [1,5]
    输出: None

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        1. 计算两个链表的长度
        2. 长的链表数值减去短的链表数值, 得出k.
        3. 长的链表先走k步.
        4. 长短链表同时向前走.
        5. 判断是否所有节点相同.

        这段代码的考虑是: 相交后又出现分叉
        """
        curr_a, count_a = headA, 1
        curr_b, count_b = headB, 1
        while curr_a.next or curr_b.next:
            if curr_a.next:
                curr_a = curr_a.next
                count_a += 1
            if curr_b.next:
                curr_b = curr_b.next
                count_b += 1

        curr_a = headA
        curr_b = headB
        k = abs(count_a - count_b)
        if count_a > count_b:
            for _ in range(k):
                curr_a = curr_a.next
        else:
            for _ in range(k):
                curr_b = curr_b.next

        same_begin = None
        while curr_a:
            if curr_a == curr_b:
                if same_begin is None:
                    same_begin = curr_a
            else:
                same_begin = None
            curr_a = curr_a.next
            curr_b = curr_b.next

        return same_begin

    def getIntersectionNode_v2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        这段代码认为, 只要相交了后续的一定是相同的.

        这段代码很简洁但是吃不透
        """
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next       # 链表交换, 是为了渐渐消除两个链表长短问题.
            p2 = headA if not p2 else p2.next       # 链表交换, 是为了渐渐消除两个链表长短问题.
        return p1


def test_1():
    l0 = ListNode(val=8)
    l0.next = ListNode(val=4)
    l0.next.next = ListNode(val=5)

    l1 = ListNode(val=4)
    l1.next = ListNode(val=1)
    l1.next.next = l0

    l2 = ListNode(val=5)
    l2.next = ListNode(val=0)
    l2.next.next = ListNode(val=1)
    l2.next.next.next = l0

    ss = Solution().getIntersectionNode(l1, l2)
    xx = ss.walk()
    assert xx == [8, 4, 5]


def main():
    test_1()


if __name__ == '__main__':
    main()
