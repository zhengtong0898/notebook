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
    剑指 Offer 22. 链表中倒数第k个节点

    输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

    例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

    示例：
    给定一个链表: 1->2->3->4->5, 和 k = 2.
    返回链表 4->5.

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
        快慢指针
        1. 先让快指针走 k 步.
        2. 慢指针从0开始走, 快指针从k开始走.
        3. 当快指针走到尾节点时, 慢指针就是倒数第k个节点.
        """
        fast = head
        while k:
            fast = fast.next
            k -= 1

        while fast:
            fast = fast.next
            head = head.next

        return head


    def getKthFromEnd_v2(self, head: ListNode, k: int) -> ListNode:
        """
        1. 先遍历一次拿到所有节点数量
        2. 计算倒数节点k位置
        3. 再遍历一次抵达k位置, 返回链表
        一次通过
        """
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1

        match = count - k
        curr = head
        count = 0
        while count != match:
            curr = curr.next
            count += 1

        return curr


def test_1():
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    l1.next.next = ListNode(val=3)
    l1.next.next.next = ListNode(val=4)
    l1.next.next.next.next = ListNode(val=5)
    ss = Solution().getKthFromEnd(l1, 2)
    xx = ss.walk()
    assert xx == [4, 5]


def main():
    test_1()


if __name__ == '__main__':
    main()
