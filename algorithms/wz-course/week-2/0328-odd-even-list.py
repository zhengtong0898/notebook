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
    给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
    请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。 请尝试使用原地算法完成。
    你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

    示例-1:
    输入: 1->2->3->4->5->NULL
    输出: 1->3->5->2->4->NULL

    示例-2:
    输入: 2->1->3->5->6->4->7->NULL
    输出: 2->3->6->7->1->5->4->NULL

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/odd-even-linked-list
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_node = ListNode()
        even_node = ListNode()
        odd_tail_node = odd_node
        even_tail_node = even_node
        count = 1
        while head:
            next_node = head.next
            head.next = None
            if count % 2:
                odd_tail_node.next = head
                odd_tail_node = odd_tail_node.next
            else:
                even_tail_node.next = head
                even_tail_node = even_tail_node.next
            head = next_node
            count += 1
        odd_tail_node.next = even_node.next
        return odd_node.next


def test_1():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ln_10.next.next = ListNode(val=3)
    ln_10.next.next.next = ListNode(val=4)
    ln_10.next.next.next.next = ListNode(val=5)
    xx = Solution().oddEvenList(ln_10).walk()
    assert xx == [1, 3, 5, 2, 4]


def test_2():
    ln_10 = ListNode(val=2)
    ln_10.next = ListNode(val=1)
    ln_10.next.next = ListNode(val=3)
    ln_10.next.next.next = ListNode(val=5)
    ln_10.next.next.next.next = ListNode(val=6)
    ln_10.next.next.next.next.next = ListNode(val=4)
    ln_10.next.next.next.next.next.next = ListNode(val=7)
    xx = Solution().oddEvenList(ln_10).walk()
    assert xx == [2, 3, 6, 7, 1, 5, 4]


def main():
    test_1()


if __name__ == '__main__':
    main()
