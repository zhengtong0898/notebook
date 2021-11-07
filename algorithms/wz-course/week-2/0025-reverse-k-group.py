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
    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

    k 是一个正整数，它的值小于或等于链表的长度。

    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

    进阶：
    你可以设计一个只使用常数额外空间的算法来解决此问题吗？
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

    示例-1:
    输入: head = [1,2,3,4,5], k = 2
    输出: [2,1,4,3,5]

    示例-2:
    输入: head = [1,2,3,4,5], k = 3
    输出: [3,2,1,4,5]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass

    def reverseKGroup_failed(self, head: ListNode, k: int) -> ListNode:
        """
        这是一个失败的写法, 无法通过 head = [1, 2], k = 2 的场景.
        """
        head_node = ListNode()
        tail_node = head_node

        final_head_node = ListNode()
        final_tail_node = final_head_node

        count = 0
        curr_node = head
        while curr_node:

            if count == k:
                count = 0
                temp_node = self.reverseList(head_node.next)
                while temp_node:
                    next_temp_node = temp_node.next
                    temp_node.next = None
                    final_tail_node.next = temp_node
                    final_tail_node = final_tail_node.next
                    temp_node = next_temp_node
                head_node = ListNode()
                tail_node = head_node

            next_node = curr_node.next
            curr_node.next = None
            tail_node.next = curr_node
            tail_node = tail_node.next
            curr_node = next_node
            count += 1

        final_tail_node.next = head_node.next
        return final_head_node.next

    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None                                # "上一个"指针节点
        curr_node = head                                # 当前指针节点
        while curr_node:                                                                             # 时间复杂度 O(n)
            next_node = curr_node.next                  # 创建临时变量保存"下一个节点"
            curr_node.next = prev_node                  # 截断 curr_node 链表, 将"上一个"节点, 链接到此处.
            prev_node = curr_node                       # 将 curr_node 存放在 prev_node 中.
            curr_node = next_node                       # curr_node 向右移动一位.
        return prev_node


def test_1():
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    l1.next.next = ListNode(val=3)
    l1.next.next.next = ListNode(val=4)
    l1.next.next.next.next = ListNode(val=5)
    ss = Solution().reverseKGroup(l1, 2)
    xx = ss.walk()
    assert xx == [2, 1, 4, 3, 5]


def test_2():
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    l1.next.next = ListNode(val=3)
    l1.next.next.next = ListNode(val=4)
    l1.next.next.next.next = ListNode(val=5)
    ss = Solution().reverseKGroup(l1, 3)
    xx = ss.walk()
    assert xx == [3, 2, 1, 4, 5]


def test_3():
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    ss = Solution().reverseKGroup(l1, 2)
    xx = ss.walk()
    assert xx == [2, 1]


def main():
    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    main()
