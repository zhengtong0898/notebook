from typing import List


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return f"<{self.__class__.__name__} val={self.val} id={id(self)} next={self.next} >"

    def walk(self) -> List[int]:
        result = []
        curr_node = self
        while curr_node:
            result.append(curr_node.val)
            curr_node = curr_node.next
        return result


class Solution:

    """
    给定一个头结点为 head 的非空单链表，返回链表的中间结点。
    如果有两个中间结点，则返回第二个中间结点。

    示例-1:
    输入：[1,2,3,4,5]
    输出：此列表中的结点 3 (序列化形式：[3,4,5])
    返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
    注意，我们返回了一个 ListNode 类型的对象 ans，这样：
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.

    示例-2:
    输入：[1,2,3,4,5,6]
    输出：此列表中的结点 4 (序列化形式：[4,5,6])
    由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/middle-of-the-linked-list
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def middleNode(self, head: ListNode) -> ListNode:
        count = 1
        curr_node = head
        while curr_node.next:
            curr_node = curr_node.next
            count += 1

        middle_index = count // 2 + 1
        count = 1
        curr_node = head
        while curr_node.next:
            if count == middle_index: return curr_node
            curr_node = curr_node.next
            count += 1

        return curr_node

    def middleNode_v2(self, head: ListNode) -> ListNode:
        # TODO: 添加快慢指针写法
        pass


def main():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ln_10.next.next = ListNode(val=3)
    ln_10.next.next.next = ListNode(val=4)
    ln_10.next.next.next.next = ListNode(val=5)
    assert ln_10.walk() == [1, 2, 3, 4, 5]
    ss = Solution().middleNode(ln_10)
    assert ss.walk() == [3, 4, 5]

    ln_10 = ListNode(val=1)
    assert ln_10.walk() == [1]
    ss = Solution().middleNode(ln_10)
    xx = ss.walk()
    assert ss.walk() == [1]


if __name__ == '__main__':
    main()
