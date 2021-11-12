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
    19. 删除链表的倒数第 N 个结点

    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

    示例-1:
    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]

    示例-2:
    输入：head = [1], n = 1
    输出：[]

    示例-3:
    输入：head = [1,2], n = 1
    输出：[1]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
        快慢指针
        1. 先让快指针走 k 步.
           特殊处理: 如果快指针还没走到 k 步就结束了, 那么就直接返回 None.
        2. 慢指针从0开始走, 快指针从k开始走(这样慢指针就能少走一步).
        3. 当快指针走到尾节点时, 慢指针就是倒数第k个节点.
        """
        fast = slow = head
        for i in range(k):
            if fast.next:
                fast = fast.next
            else:
                return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head

    def getKthFromEnd_v2(self, head: ListNode, k: int) -> ListNode:
        """
        快慢指针
        1. 先让快指针走 k+1 步.
        2. 慢指针从0开始走, 快指针从k开始走(这样慢指针就能少走一步).
        3. 当快指针走到尾节点时, 慢指针就是倒数第k个节点.
        这个写法有很多细节不通, 因为 test_2() 和 test_4() 这种场景走不通.
        """
        k += 1
        fast = slow = head
        while k:
            fast = fast.next
            k -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


def test_1():
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    l1.next.next = ListNode(val=3)
    l1.next.next.next = ListNode(val=4)
    l1.next.next.next.next = ListNode(val=5)
    ss = Solution().getKthFromEnd_v2(l1, 2)
    xx = ss.walk()
    assert xx == [1, 2, 3, 5]


def test_2():
    l1 = ListNode(val=1)
    ss = Solution().getKthFromEnd(l1, 1)
    assert ss is None


def test_3():
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    ss = Solution().getKthFromEnd(l1, 1)
    xx = ss.walk()
    assert xx == [1]


def test_4():
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    ss = Solution().getKthFromEnd(l1, 2)
    xx = ss.walk()
    assert xx == [2]


def main():
    test_1()
    test_2()
    test_4()


if __name__ == '__main__':
    main()
