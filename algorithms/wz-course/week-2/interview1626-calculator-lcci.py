

class Solution:

    """
    面试题 16.26. 计算器

    给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。
    表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

    示例-1:
    输入: "3+2*2"
    输出: 7

    示例-2:
    输入: " 3/2 "
    输出: 1

    示例-3:
    输入: " 3+5 / 2 "
    输出: 5

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/calculator-lcci
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def calculate(self, s: str) -> int:
        """
        栈解法

        1. 移除所有空元素
        2. 进入循环
        3.   设法读取完整数字, 数字可能不知一位.
        4.   再取下一个(已知是加减乘除符号)元素.
        5.   乘除法优先处理
        6. 进入循环
        7.   统一做加法处理.
        """
        count = 0
        stack = []
        prev_operator = ""

        s = s.replace(" ", "")
        while count < len(s):

            # 整数可能不止一位, 需要把整数取完整
            num = ""
            while count < len(s) and s[count].isdigit():
                num += s[count]
                count += 1
            num = int(num)

            # 后置一次循环处理.
            # 乘法和除法的优先级高，先处理
            if prev_operator == "+":
                stack.append(num)
            elif prev_operator == "-":
                stack.append(-num)                  # 把减法全换成加法统一处理.
            elif prev_operator == "*":
                stack.append(stack.pop() * num)
            elif prev_operator == "/":
                stack.append(int(stack.pop() / num))
            else:
                stack.append(num)

            # 尝试在往前走一步, 取下一个字符(已知是加减乘除符号).
            if count < len(s):
                next_char = s[count]
                prev_operator = next_char

            count += 1

        # 统一做加法处理.
        result = 0
        while stack:
            result += stack.pop()

        return result

    def calculate_error(self, s: str) -> int:
        """
        超出时间限制.
        没仔细看题，不让使用 eval.
        """
        s = s.replace(" ", "")

        priority_map = {"+": 1, "-": 1, "*": 2, "/": 2}
        dig_stack = []
        op_stack = []

        count = 0
        dig = ""
        while count < len(s):
            i = s[count]
            if i.isdigit():
                dig += i
            elif i in ["+", "-", "*", "/"]:
                if dig:
                    dig_stack.append(int(dig))
                    dig = ""

                prev_op = op_stack[len(op_stack)-1:len(op_stack)]
                if not prev_op:
                    op_stack.append(i)
                    count += 1
                    continue

                prev_op = prev_op[0]
                if priority_map[prev_op] == 2:
                    right = dig_stack.pop()
                    op = op_stack.pop()
                    left = dig_stack.pop()
                    value = int(eval(f"{left} {op} {right}"))
                    dig_stack.append(value)
                elif prev_op == i:
                    left = dig_stack.pop(0)
                    op = op_stack.pop(0)
                    right = dig_stack.pop(0)
                    value = int(eval(f"{left} {op} {right}"))
                    dig_stack.insert(0, value)

                op_stack.append(i)

            count += 1

        if dig:
            dig_stack.append(int(dig))

        prev_op = op_stack[len(op_stack)-1:len(op_stack)]
        if prev_op and priority_map[prev_op[0]] == 2:
            right = dig_stack.pop()
            op = op_stack.pop()
            left = dig_stack.pop()
            value = int(eval(f"{left} {op} {right}"))
            dig_stack.append(value)

        if len(dig_stack) > 1 and not op_stack:
            return int(s)

        while len(dig_stack) > 1:
            left = dig_stack.pop(0)
            op = op_stack.pop(0)
            right = dig_stack.pop(0)
            value = eval(f"{left} {op} {right}")
            dig_stack.insert(0, value)

        return dig_stack.pop()


def main():
    ss = Solution().calculate("3+2*2")
    assert ss == 7
    ss = Solution().calculate(" 3/2 ")
    assert ss == 1
    ss = Solution().calculate(" 3+5 / 2 ")
    assert ss == 5
    ss = Solution().calculate("42")
    assert ss == 42
    ss = Solution().calculate("0-2147483647")
    assert ss == -2147483647
    ss = Solution().calculate("1-1+1")
    assert ss == 1
    ss = Solution().calculate("1+1-1")
    assert ss == 1
    ss = Solution().calculate("1*2-3/4+5*6-7*8+9/10")
    assert ss == -24


if __name__ == '__main__':
    main()
