

class Solution:

    """
    20. 有效的括号

    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

    示例-1:
    输入：s = "()"
    输出：true

    示例-2:
    输入：s = "()[]{}"
    输出：true

    示例-3:
    输入：s = "(]"
    输出：false

    示例-4:
    输入：s = "([)]"
    输出：false

    示例-5:
    输入：s = "{[]}"
    输出：true

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/valid-parentheses
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def isValid(self, s: str) -> bool:
        left_stack = []
        char_map = {"]": "[", "}": "{", ")": "("}
        for char in s:                                  # 从左往右遍历
            if char in char_map.values():               # 将左侧字符添加到 left_stack
                left_stack.append(char)
            elif char in char_map.keys():               # 右侧字符, 需要特殊处理
                if not left_stack:                      # 1). 当遇到右侧字符时, left_stack 理论上不能为空.
                    return False
                if char_map[char] != left_stack.pop():  # 2). 右侧字符所对应的左侧字符, 必须要等于 left_stack 的尾元素.
                    return False
            else:                                       # 即不是左侧字符，也不是右侧字符.
                return False
        return left_stack == []

    def isValid_error(self, s: str) -> bool:
        """
        关键词-1: 左括号必须用相同类型的
        关键词-2: 左括号必须以正确的顺序闭合。

        失败场景: (([]){})
        """
        if len(s) < 2: return False
        if len(s) % 2: return False

        key_map = {"{": "}", "[": "]", "(": ")"}
        key_right = ["}", "]", ")"]
        key_left = ["{", "[", "("]

        s = list(s)
        right_stack = []
        while len(s) > 1:
            right_value = s.pop()
            left_value = s[-1]
            if key_map.get(left_value) == right_value:
                s.pop()
                continue

            if right_value not in key_right:
                return False
            right_stack.append(right_value)

        if len(s) != len(right_stack): return False

        while s:
            left_value = s.pop()
            right_value = right_stack.pop()
            if key_map.get(left_value) != right_value:
                return False

        return True


def main():
    assert Solution().isValid("()") is True
    assert Solution().isValid(")(") is False
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False
    assert Solution().isValid("{[]}") is True
    assert Solution().isValid("(){}}{") is False
    assert Solution().isValid("()))") is False
    assert Solution().isValid("(([]){})") is True


if __name__ == '__main__':
    main()
