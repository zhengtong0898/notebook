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
    剑指 Offer 06. 从尾到头打印链表 （简单）

    输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

    示例-1:
    输入：head = [1,3,2]
    输出：[2,3,1]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.result = []
        self.end = False

    def reversePrint(self, head: ListNode) -> List[int]:
        """
        解题思路

        在没有学习递归之前, 可以采用头插入的方式完成链表的反转, 然后再将链表循环打印出来.
        但学习了递归之后, 可以采用简单递归压栈形式去完成反向链表值.
        递归关键点:
        层层递进走到链表末端节点,
        层层回归将每层节点的值append到列表中.
        """
        dummy_head = ListNode(next_=head)
        self.recursion(dummy_head)
        return self.result

    def recursion(self, head: ListNode):
        if head.next is None:
            self.end = True
            return head.val

        head_next = head.next
        ss = self.recursion(head_next)              # 1.1 这里承接上一个递归函数的结果,
        self.result.append(ss)                      # 1.1 然后将上一个结果写入结果集.
        return head.val                             # 1.0 这返回的值, 将会被下一个堆栈(1.1)的递归函数处理.


def main():
    head = ListNode(val=1)
    head.next = ListNode(val=3)
    head.next.next = ListNode(val=2)
    ss = Solution().reversePrint(head)
    assert ss == [2, 3, 1]


if __name__ == '__main__':
    main()
