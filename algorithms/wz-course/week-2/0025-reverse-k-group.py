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
    0025. K 个一组翻转链表

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

    def reverseKGroup(self, head, k):
        """
        https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
        """
        # 虚拟头节点、虚拟尾节点
        dummy_head = ListNode(next_=head)
        dummy_tail = dummy_head

        # 实际头节点、实际尾结点
        left = right = head
        while True:
            # real_tail 尾节点 持续右移,
            # 当 count == k 时, 满足 reverse 的条件, 跳出二级while循环.
            count = 0
            while right and count < k:
                right = right.next
                count += 1

            # 当 count != k 时, 满足结束条件, 跳出一级while循环.
            if count != k:
                return dummy_head.next

            # 执行 reverse 操作.
            prev, curr = right, left
            for _ in range(k):
                # curr.next, prev, curr = prev, curr, curr.next
                # 假设链表是: 1 -> 2 -> 3 -> 4 -> 5
                # 禁止使用这种写法, 容易把人绕进去, 因为如果直接将代码拆分成:
                # curr.next = prev                                                        # curr = 1 -> 4 -> 5
                # prev = curr                                                             # prev = 1 -> 4 -> 5
                # curr = curr.next                                                        # curr = 4 -> 5
                # 这种拆分写法会在第二次循环的时候就造成环引用问题.
                # 如果不拆分则不存在环引用问题, 这很费解.
                # 经过查阅资料得知: Python内部会帮建立一个栈来保存变量,
                # 这也算是临时变量了, 然后再根据实际情况来决定如何交换变量.
                # 参考资料:
                # https://www.zhihu.com/question/63859022
                # https://blog.csdn.net/hanzheng992/article/details/52430475
                # https://stackoverflow.com/a/47529318
                # https://www.jianshu.com/p/bf5819490120
                curr_next = curr.next                                                     # curr_next = 2 -> 3 -> 4 -> 5
                curr.next = prev                                                          # curr = 1 -> 4 -> 5
                prev = curr                                                               # prev = 1 -> 4 -> 5
                curr = curr_next                                                          # curr = 2 -> 3 -> 4 -> 5

            # 链接后续节点
            # dummy_tail.next, dummy_tail, real_head = prev, real_head, real_tail         # connect two k-groups
            # 由于这里并没有产生环引用，所以可以直接拆分赋值语句
            dummy_tail.next = prev                                                        # 3 -> 2 -> 1 -> 4 -> 5
            dummy_tail = left                                                             # 1 -> 4 -> 5
            left = right                                                                  # 4 -> 5

    def reverseKGroup_idiomatic(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:                                                           # use r to locate the range
                r = r.next
                count += 1
            if count == k:                                          # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    # 难点在这里, 这里有涉及到嵌套, 参考上面的拆解.
                    cur.next, cur, pre = pre, cur.next, cur                                         # standard reversing
                jump.next, jump, l = pre, l, r                                                    # connect two k-groups
            else:
                return dummy.next


def test_1():
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    l1.next.next = ListNode(val=3)
    l1.next.next.next = ListNode(val=4)
    l1.next.next.next.next = ListNode(val=5)
    ss = Solution().reverseKGroup(l1, 3)
    xx = ss.walk()
    assert xx == [3, 2, 1, 4, 5]


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
