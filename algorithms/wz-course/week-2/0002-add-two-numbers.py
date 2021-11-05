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
    给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

    请你将两个数相加，并以相同形式返回一个表示和的链表。

    你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


    示例-1:
    输入: l1 = [2, 4, 3]
         l2 = [5, 6, 4]
    输出: [7, 0 ,8]
    解释: 342 + 465 = 807


    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/add-two-numbers
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        解题思路:
        由于 l1 和 l2 两个链表本身就是逆序,
        所以 l1 和 l2 的链表头的值对应的是个位数,
        因此 l1 和 l2 可以同时从开始位置一直相加, 同时进入下一个位置,
        需要注意的是, 当两个数相加大于9时, 下一个位置需要递增1,
        这符合小学加法的计算逻辑.

        遍历三要素
        指针初始: l1 = l1, l2 = l2, increment = 0;
        遍历结束: (l1 is None or l2 is None) and increment == 0
        遍历逻辑: 两数相加, 如果数值大于9, 则 increment = 1;
                 l1 和 l2 都向右移动一位.
        """
        increment = 0
        head_node = ListNode()
        tail_node = head_node
        while l1 or l2 or increment > 0:
            l1 = ListNode(val=0) if l1 is None else l1
            l2 = ListNode(val=0) if l2 is None else l2
            val = l1.val + l2.val + increment
            increment = 1 if val > 9 else 0
            val = val % 10
            tail_node.next = ListNode(val=val)
            tail_node = tail_node.next
            l1 = l1.next
            l2 = l2.next

        return head_node.next


def test_1():
    l1 = ListNode(val=2)
    l1.next = ListNode(val=4)
    l1.next.next = ListNode(val=3)
    l2 = ListNode(val=5)
    l2.next = ListNode(val=6)
    l2.next.next = ListNode(val=4)
    ss = Solution().addTwoNumbers(l1, l2)
    xx = ss.walk()
    assert xx == [7, 0, 8]


def test_2():
    l1 = ListNode(val=0)
    l2 = ListNode(val=0)
    ss = Solution().addTwoNumbers(l1, l2)
    xx = ss.walk()
    assert xx == [0]


def test_3():
    l1 = ListNode(val=9)
    l1.next = ListNode(val=9)
    l1.next.next = ListNode(val=9)
    l1.next.next.next = ListNode(val=9)
    l1.next.next.next.next = ListNode(val=9)
    l1.next.next.next.next.next = ListNode(val=9)
    l1.next.next.next.next.next.next = ListNode(val=9)
    l2 = ListNode(val=9)
    l2.next = ListNode(val=9)
    l2.next.next = ListNode(val=9)
    l2.next.next.next = ListNode(val=9)
    ss = Solution().addTwoNumbers(l1, l2)
    xx = ss.walk()
    assert xx == [8, 9, 9, 9, 0, 0, 0, 1]


def main():
    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    main()
