

# 题目链接
# https://leetcode-cn.com/problems/add-two-numbers/
class ListNode(object):
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class AddTwoNumbers(object):

    def add_two_numbers(self, left_node, right_node):
        """
        :type left_node: ListNode
        :type right_node: ListNode
        :rtype: ListNode
        """

        # 引用:
        # 当 current 修改 val 或 next 时, root会跟着发生变化, 因为它们都引用相同的对象.
        # 但是当 current 变量被覆盖时, root不会发生任何变化.
        root = current = ListNode(0)
        carry = 0

        # 当  left_node is not None 时, 表示它还没有到末尾.
        # 当 right_node is not None 时, 表示它还没有到末尾.
        # 当 carry != 0 时, 表示它仍需再循环一次.
        while left_node or left_node or carry:

            if left_node:
                carry += left_node.val                          # 同步追加
                left_node = left_node.next                      # 切换下一个节点

            if right_node:
                carry += right_node.val                         # 同步追加
                right_node = right_node.next                    # 切换下一个节点

            # carry % 10 = 取余, 得到的是计算后的个位数的值.
            current.next = ListNode(carry % 10)                 # 持续建立新的链节点
            current = current.next                              # 切换链节点
            carry = int(carry / 10)                             # 逢十进一, 得到的是计算后的十位的值.

        return root.next


def test_1():
    left_node = ListNode(2)
    left_node.next = ListNode(4)
    left_node.next.next = ListNode(3)

    right_node = ListNode(5)
    right_node.next = ListNode(6)
    right_node.next.next = ListNode(1)

    atn = AddTwoNumbers()
    ss = atn.add_two_numbers(left_node, right_node)
    assert ss.val == 7
    assert ss.next.val == 0
    assert ss.next.next.val == 5


def test_2():
    left_node = ListNode(2)
    left_node.next = ListNode(4)
    left_node.next.next = ListNode(3)
    left_node.next.next.next = ListNode(8)

    right_node = ListNode(5)
    right_node.next = ListNode(6)
    right_node.next.next = ListNode(4)

    atn = AddTwoNumbers()
    ss = atn.add_two_numbers(left_node, right_node)
    assert ss.val == 7
    assert ss.next.val == 0
    assert ss.next.next.val == 8
    assert ss.next.next.next.val == 8


def main():
    test_1()
    test_2()


if __name__ == '__main__':
    main()
