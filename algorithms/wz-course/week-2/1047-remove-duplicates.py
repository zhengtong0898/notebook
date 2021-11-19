
class Solution:

    """
    1047. 删除字符串中的所有相邻重复项

    给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
    在 S 上反复执行重复项删除操作，直到无法继续删除。
    在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

    示例-1:
    输入："abbaca"
    输出："ca"
    解释：
    例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
    之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def removeDuplicates(self, s: str) -> str:
        """
        思路:
        1. s 从左往右遍历.
        2. 先将 s leftmost 元素加入到 stack 中,
        3. 下一次循环计算中, s rightmost 和 stack rightmost 进行比较,
        4. 如果相同直接消除掉 stack rightmost 元素.

        优化点:
        由于 s 从左往右进行比较和操作,
        所以最终的结果是一个正序的栈,
        只需要join将stack转成字符串即可.

        严格意义上的问题:
        stack 只能 pop,
        所以这里应该使用 list.
        """
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

    def removeDuplicates_v2_optimize(self, s: str) -> str:
        """
        在 removeDuplicates_v2 基础上, 展开优化.

        removeDuplicates_v2 的问题点:
        尝试从 s 中直接走两步进行判断,
        如果相同直接消除(效率高),
        但如果不相同, 则将 rightmost 元素添加到 stack 中, 这里会产生出来一个问题,
        就是下一次循环计算, 需要先那 rightmost 和 stack rightmost 元素先比较,
        如果相同则消除掉 stack rightmost 元素,
        如果不相同则再尝试从 s 中走两步进行判断.

        优化点:
        不要从 s 中直接走两步来判断,
        先将 s rightmost 元素加入到 stack 中,                                    (效率高, 代码可以重复被使用)
        下一次循环计算中, s rightmost 和 stack rightmost 进行比较,
        如果相同直接消除掉 stack rightmost 元素.                                  (效率高, 代码可以重复被使用).

        优化后仍然存在问题:
        这个代码采取的是 s 从右往左进行比较和操作,
        这样带来的一个问题是, 最终结果是一个倒序的字符串,
        要么通过reversed函数反转一次, 要么再写一个循环pop出来配合join合并一下.
        """
        n = len(s)
        stack = []
        while n:
            rightmost = s[n-1]
            if stack and stack[-1] == rightmost:
                stack.pop()
            else:
                stack.append(rightmost)
            n -= 1
        return "".join([stack.pop() for i in range(len(stack))])

    def removeDuplicates_v2(self, s: str) -> str:
        """
        O(n)遍历 + 栈 解法
        注意，这里是两个相邻的书消掉即可, 不是连续的字符消除.

        这里的想法和思路是:
        1. 在 s 中走两个步, 如果相同则消掉, 如果不同则将最右边的元素添加到stack中.
        2. 然后再用 s 最右元素 与 stack中最右元素相比较.
        """
        n = len(s) - 1
        stack = []
        while n >= 0:
            right = s[n]

            if len(stack):
                left = stack.pop()
                if right == left:
                    n -= 1
                    continue
                else:
                    stack.append(left)

            left = s[n-1] if n - 1 >= 0 else None
            if right == left:
                n -= 1
            else:
                stack.append(right)

            n -= 1

        ns = ""
        while stack:
            ns += stack.pop()

        return ns


def main():
    ss = Solution().removeDuplicates_v2_optimize("abbaca")
    assert ss == "ca"
    ss = Solution().removeDuplicates_v2_optimize("aaaaaaaaa")
    assert ss == "a"


if __name__ == '__main__':
    main()
