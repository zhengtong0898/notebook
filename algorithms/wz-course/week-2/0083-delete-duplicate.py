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
    存在一个按升序排列的链表，给你这个链表的头节点 head ，
    请你删除所有重复的元素，使每个元素 只出现一次 。
    返回同样按升序排列的结果链表。

    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        遍历三要素

        指针初始: head_node, tail_node;                     # 作为返回对象的头尾节点, 并利用虚拟头节点特性.
                 curr_node, next_node;                     # 作为指针游标, 也利用虚拟头节点特性.
        遍历结束: next_node is None;                        # 当下一个节点为None时，跳出循环.
        遍历逻辑: ...                                       # 当 curr_node.val == next_node.val 时,
                                                           # curr_node 游标不动, next_node 游标右移一位.ß
                                                           #
                                                           # 当 curr_node.val != next_node.val 时, 看下面的描述.
        """

        if not head: return head

        head_node = ListNode(val=-1)
        tail_node = head_node

        curr_node = ListNode(val=-1, next_=head)
        next_node = curr_node.next

        while next_node:
            if curr_node.val == next_node.val:
                next_node = next_node.next
            else:
                curr_node = next_node

                next_node_next = next_node.next     # 1. 创建临时变量保存 next_node 链表的后续节点
                next_node.next = None               # 2. 截断 next_node, 使其变成一个 "尾节点" 状态
                tail_node.next = next_node          # 3. 将 "尾节点" 赋值给 tail_node.next
                tail_node = tail_node.next          # 4. 此时 tail_node 链表有两个节点, 为了让他依旧是尾节点, 它需要右移一位.
                next_node = next_node_next          # 5. 恢复 next_node, 右移一位.

        return head_node.next

    def deleteDuplicates_v2(self, head: ListNode) -> ListNode:
        """
        leet-code 162 / 166 失败

        输入: [1, 1]
        输出: [1, 1]
        期望: [1]
        """
        if not head: return head
        head_node = ListNode(next_=head)
        tail_node = head_node.next
        curr_node = head
        next_node = head.next
        while next_node:
            if curr_node.val == next_node.val:
                next_node = next_node.next
            else:
                curr_node = next_node
                next_node_next = next_node.next
                next_node.next = None
                tail_node.next = next_node
                tail_node = tail_node.next
                next_node = next_node_next

        return head_node.next


def test_1():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=1)
    ln_10.next.next = ListNode(val=2)
    ss = Solution().deleteDuplicates(ln_10)
    xx = ss.walk()
    assert xx == [1, 2]


def test_2():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=1)
    ln_10.next.next = ListNode(val=2)
    ln_10.next.next.next = ListNode(val=3)
    ln_10.next.next.next.next = ListNode(val=3)
    ss = Solution().deleteDuplicates(ln_10)
    xx = ss.walk()
    assert xx == [1, 2, 3]


def test_3():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=1)
    ss = Solution().deleteDuplicates(ln_10)
    xx = ss.walk()
    assert xx == [1]


def test_4():
    ln_10 = ListNode(val=0)
    ln_10.next = ListNode(val=0)
    ln_10.next.next = ListNode(val=0)
    ln_10.next.next.next = ListNode(val=0)
    ss = Solution().deleteDuplicates(ln_10)
    xx = ss.walk()
    assert xx == [0]


def main():
    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    main()
